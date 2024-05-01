# https://github.com/microsoft/phyagi-vllm/commit/778713744c9554a98fd5a988332a44069c360062

from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="<model path>",trust_remote_code=True)

outputs = llm.generate(prompts, sampling_params)

# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")



# example amlt_run.yaml
# description: vllm_phi_debug

# target:
#   service: sing
#   name: aims-sing-east-us2
#   workspace_name: aims-sing-res-eu-WS

# environment:
#   image: pytorch/pytorch:2.1.2-cuda12.1-cudnn8-devel

# code:
#   local_dir: ./

# storage:
#   output:
#     storage_account_name: genaimsra
#     container_name: models
#     mount_dir: /genaimsra/models

# jobs:
#   - name: debug
#     sku: G1
#     command:
#       - pip install -e .
#       - python ./test.py
#     sla_tier: Premium
#     priority: high