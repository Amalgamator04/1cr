# 🚀 Complete Fine-Tuning Script for Llama Guard 3 with Your Data

import json
from unsloth import FastLanguageModel
import torch
from trl import SFTTrainer
from transformers import TrainingArguments
from datasets import Dataset

def prepare_dataset(json_file_path):
    """
    Convert your JSON data to the format required for Llama Guard 3 fine-tuning
    """
    # Read your JSON data
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Convert to training format
    training_data = []
    for item in data:
        # Assuming your JSON has 'text' and 'label' fields
        text = item.get('text', '')
        label = item.get('label', 'safe')
        
        # Convert label to Llama Guard format
        if label == 'hate':
            response = "unsafe\nS10"  # S10 is hate speech category
        elif label == 'neutral':
            response = "unsafe\nS2"   # S2 for offensive but not hate
        else:
            response = "safe"
        
        # Format as conversation
        conversation = {
            "conversations": [
                {"from": "human", "value": text},
                {"from": "gpt", "value": response}
            ]
        }
        training_data.append(conversation)
    
    return Dataset.from_list(training_data)

def fine_tune_llama_guard():
    """
    Fine-tune Llama Guard 3 1B for Hindi hate speech detection
    """
    print("🚀 Starting Llama Guard 3 fine-tuning...")
    
    # 1. Load the model
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name="meta-llama/Llama-Guard-3-1B",
        max_seq_length=2048,
        dtype=None,
        load_in_4bit=True,
    )
    
    # 2. Apply LoRA for efficient training
    model = FastLanguageModel.get_peft_model(
        model,
        r=16,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                       "gate_proj", "up_proj", "down_proj"],
        lora_alpha=16,
        lora_dropout=0,
        bias="none",
        use_gradient_checkpointing="unsloth",
        random_state=3407,
    )
    
    # 3. Prepare your dataset
    print("📊 Preparing dataset...")
    dataset = prepare_dataset("E:/1cr/data.json")
    
    # 4. Set up training
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=dataset,
        dataset_text_field="conversations",
        max_seq_length=2048,
        dataset_num_proc=2,
        args=TrainingArguments(
            per_device_train_batch_size=2,
            gradient_accumulation_steps=4,
            warmup_steps=5,
            num_train_epochs=3,  # Adjust based on your dataset size
            learning_rate=2e-4,
            fp16=not torch.cuda.is_available(),
            bf16=torch.cuda.is_available(),
            logging_steps=1,
            optim="adamw_8bit",
            weight_decay=0.01,
            lr_scheduler_type="linear",
            seed=3407,
            output_dir="outputs",
            save_steps=50,
        ),
    )
    
    # 5. Start training
    print("🔥 Starting training...")
    trainer.train()
    
    # 6. Save the model
    print("💾 Saving fine-tuned model...")
    model.save_pretrained("llama_guard_hindi_ft")
    tokenizer.save_pretrained("llama_guard_hindi_ft")
    
    # 7. Export to GGUF format for Ollama
    print("📦 Converting to GGUF format for Ollama...")
    model.save_pretrained_gguf("llama_guard_hindi", tokenizer, quantization_method="q4_k_m")
    
    print("✅ Fine-tuning complete!")
    print("📁 Files saved:")
    print("   - llama_guard_hindi_ft/ (PyTorch format)")
    print("   - llama_guard_hindi.gguf (For Ollama)")
    
    return model, tokenizer

def create_ollama_modelfile():
    """
    Create Modelfile for Ollama import
    """
    modelfile_content = """FROM ./llama_guard_hindi.gguf

TEMPLATE \"\"\"<|begin_of_text|><|start_header_id|>user<|end_header_id|>
{{ .Prompt }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
\"\"\"

PARAMETER temperature 0.1
PARAMETER top_k 1
PARAMETER top_p 0.95
PARAMETER stop "<|eot_id|>"
PARAMETER stop "<|end_of_text|>"

SYSTEM \"\"\"You are Llama Guard 3, a content safety classifier. Classify the given input as 'safe' or 'unsafe'. If unsafe, specify the category (S1-S13). Focus particularly on hate speech (S10).\"\"\"
"""
    
    with open("Modelfile", "w") as f:
        f.write(modelfile_content)
    
    print("📝 Modelfile created for Ollama import")

def test_model_inference(model, tokenizer, test_text):
    """
    Test the fine-tuned model
    """
    print(f"\n🧪 Testing model with: '{test_text}'")
    
    # Format input
    formatted_input = f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n{test_text}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"
    
    # Tokenize and generate
    inputs = tokenizer(formatted_input, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=10,
            temperature=0.1,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    print(f"🎯 Model response: {response}")
    
    return response

if __name__ == "__main__":
    try:
        # Step 1: Fine-tune the model
        model, tokenizer = fine_tune_llama_guard()
        
        # Step 2: Create Ollama Modelfile
        create_ollama_modelfile()
        
        # Step 3: Test the model
        test_cases = [
            "तुम एक बेकार इंसान हो",  # Should be unsafe S10
            "आज का मौसम अच्छा है",     # Should be safe
            "मैं तुमसे नफरत करता हूँ"  # Should be unsafe S10
        ]
        
        FastLanguageModel.for_inference(model)
        for test_text in test_cases:
            test_model_inference(model, tokenizer, test_text)
        
        print("\n🎉 FINE-TUNING COMPLETE!")
        print("\n📋 Next steps:")
        print("1. Import to Ollama: ollama create llama-guard3-hindi-hate:ft -f Modelfile")
        print("2. Run: ollama run llama-guard3-hindi-hate:ft")
        print("3. Test with your Hindi text!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure you have:")
        print("   - GPU with enough memory (8GB+ recommended)")
        print("   - Proper data format in E:/1cr/data.json")
        print("   - All dependencies installed")