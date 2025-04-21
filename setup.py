from setuptools import setup, find_namespace_packages

setup(
    name='gpt_sovits',
    version='4.0.0',  # Update version number as needed
    description='A Powerful Few-shot Voice Conversion and Text-to-Speech WebUI.',
    author='RVC-Boss',
    url='https://github.com/JBlackN/GPT-SoVITS',
    packages=find_namespace_packages(include=['GPT_SoVITS', 'GPT_SoVITS.*', 'tools', 'tools.*']),
    include_package_data=True,
    package_data={
        'GPT_SoVITS': ['**/*'],
        'tools.i18n': ['locale/*.json'],
    },
    install_requires=[
        "numpy<2.0",
        "scipy",
        "tensorboard",
        "librosa==0.9.2",
        "numba",
        "pytorch-lightning>=2.4",
        "gradio>=4.41,<5",
        "ffmpeg-python",
        "onnxruntime; sys_platform == 'darwin'",
        "onnxruntime-gpu; sys_platform != 'darwin'",
        "tqdm", # Note: tqdm was listed twice, consolidated here
        "funasr==1.0.27",
        "cn2an",
        "pypinyin",
        "pyopenjtalk>=0.4.1",
        "g2p_en",
        "torchaudio",
        "modelscope==1.10.0",
        "sentencepiece",
        "transformers>=4.43",
        "peft",
        "chardet",
        "PyYAML",
        "psutil",
        "jieba_fast",
        "jieba",
        "split-lang",
        "fast_langdetect>=0.3.1",
        "wordsegment",
        "rotary_embedding_torch",
        "ToJyutping", # Keep capitalization as in requirements.txt
        "g2pk2",
        "ko_pron",
        "opencc; sys_platform != 'linux'",
        "opencc==1.1.1; sys_platform == 'linux'",
        "python_mecab_ko; sys_platform != 'win32'",
        "fastapi[standard]>=0.115.1", # Includes the extra '[standard]'
        "x_transformers",
        "torchmetrics<=1.5",
        "pydantic<=2.10.6",
        "ctranslate2>=4.0,<5",
        "huggingface_hub>=0.13",
        "tokenizers>=0.13,<1",
        "av>=11",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update based on actual license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',  # Specify the appropriate Python version
)