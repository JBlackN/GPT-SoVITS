from setuptools import setup, find_namespace_packages

setup(
    name='gpt_sovits',
    version='0.0.1',  # Update version number as needed
    description='A Powerful Few-shot Voice Conversion and Text-to-Speech WebUI.',
    author='RVC-Boss',
    url='https://github.com/JBlackN/GPT-SoVITS',
    packages=find_namespace_packages(include=['GPT_SoVITS', 'GPT_SoVITS.*', 'AR', 'AR.*', 'tools', 'tools.*']),
    include_package_data=True,
    install_requires=[
        'numpy==1.23.4',
        'scipy',
        'tensorboard',
        'librosa==0.9.2',
        'numba==0.56.4',
        'pytorch-lightning',
        'gradio>=4.0,<=4.24.0',
        'ffmpeg-python',
        'tqdm',
        'funasr==1.0.27',
        'cn2an',
        'pypinyin',
        'pyopenjtalk>=0.3.4',
        'g2p_en',
        'torchaudio',
        'modelscope==1.10.0',
        'sentencepiece',
        'transformers',
        'chardet',
        'PyYAML',
        'psutil',
        'jieba_fast',
        'jieba',
        'LangSegment>=0.2.0',
        'Faster_Whisper',
        'wordsegment',
        'rotary_embedding_torch',
        'ToJyutping',
        'g2pk2',
        'ko_pron',
        'fastapi<0.112.2'
    ],
    extras_require={
        'darwin': ['onnxruntime'],
        'linux': ['opencc==1.1.1'],
        'non_darwin': ['onnxruntime-gpu'],
        'non_linux': ['opencc'],
        'non_windows': ['python_mecab_ko']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update based on actual license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',  # Specify the appropriate Python version
)
