from dataclasses import dataclass
from fastT5 import get_onnx_model
from transformers import AutoTokenizer


@dataclass
class CommitMessageGenerator:
    model_name = "SEBIS/code_trans_t5_base_commit_generation_transfer_learning_finetune"
    models_folder = "models/ct-base-commits-fastt5-quantized"

    def __post_init__(self):
        print("Loading model...")
        self.model = get_onnx_model(self.model_name, self.models_folder)
        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, max_length=512)
        print("Done")

    def generate(self, diff):
        token = self.tokenizer(
            diff, 
            return_tensors='pt', 
            truncation=True,
            max_length=512
        )
        tokens = self.model.generate(
            input_ids=token['input_ids'],
            attention_mask=token['attention_mask'],
            num_beams=2,
            max_new_tokens=20,
        )
        return self.tokenizer.decode(
            tokens.squeeze(), 
            skip_special_tokens=True
        )
    
    def post_process(self, message: str) -> str:
        message = message.capitalize()
        message, *_ = message.split(".")
        return message
    
    def __call__(self, diff: str) -> str:
        return self.post_process(self.generate(diff))
