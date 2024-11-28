from PIL import Image
from transformers import AutoProcessor
from vllm import LLM, SamplingParams
from qwen_vl_utils import process_vision_info

class InferlessPythonModel:
  def initialize(self):
      
        self.llm = LLM(
            model='Qwen/Qwen2-VL-7B-Instruct',
            limit_mm_per_prompt={'image': 10},
        )
        self.processor = AutoProcessor.from_pretrained('Qwen/Qwen2-VL-7B-Instruct')
      
  def infer(self, inputs):
        prompt = inputs["prompt"] #'What does this diagram illustrate?'
        image_url = inputs["image_url"]
        system_prompt = inputs.get("system_prompt","You are a helpful assistant.")
        temperature = float(inputs.get("temperature",0.7))
        top_p = float(inputs.get("top_p",0.1))
        repetition_penalty = float(inputs.get("repetition_penalty",1.18))
        top_k = int(inputs.get("top_k",40))
        max_tokens = int(inputs.get("max_tokens",256))
        max_pixels = int(inputs.get("max_pixels",12845056))
        print("=="*200,prompt,
        image_url,
        system_prompt,
        temperature,
        top_p,
        repetition_penalty,
        top_k,
        max_tokens,
        max_pixels,flush=True)
        sampling_params = SamplingParams(temperature=temperature,top_p=top_p,repetition_penalty=repetition_penalty,
                                         top_k=top_k,max_tokens=max_tokens)
      
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': [
                {
                    'type': 'image',
                    'image': image_url,
                    'max_pixels': max_pixels,
                },

                {
                    'type': 'text',
                    'text': prompt,
                },
            ]},
        ]
        prompt = self.processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )
        image_inputs, video_inputs = process_vision_info(messages)
        
        mm_data = {}
        mm_data['image'] = image_inputs
        
        llm_inputs = {
            'prompt': prompt,
            'multi_modal_data': mm_data,
        }
        
        outputs = self.llm.generate([llm_inputs], sampling_params=sampling_params)
        generated_text = outputs[0].outputs[0].text
        
        return {"generated_result": generated_text}

  def finalize(self):
    self.llm = None
