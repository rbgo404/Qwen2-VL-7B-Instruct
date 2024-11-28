INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["What does this diagram illustrate?"]
    },
    "image_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"]
    },
    "system_prompt": {
        'datatype': 'STRING',
        'required': False,
        'shape': [1],
        'example': ["You are a helpful coding bot."]
    },
    "temperature": {
        'datatype': 'FP64',
        'required': False,
        'shape': [1],
        'example': [0.7]
    },
    "top_p": {
        'datatype': 'FP64',
        'required': False,
        'shape': [1],
        'example': [0.1]
    },
    "repetition_penalty": {
        'datatype': 'FP64',
        'required': False,
        'shape': [1],
        'example': [1.18]
    },
    "max_tokens": {
        'datatype': 'INT64',
        'required': False,
        'shape': [1],
        'example': [256]
    },
    "max_pixels": {
        'datatype': 'INT64',
        'required': False,
        'shape': [1],
        'example': [12845056]
    },
    "top_k":{
        'datatype': 'INT64',
        'required': False,
        'shape': [1],
        'example': [40]
    }
}
