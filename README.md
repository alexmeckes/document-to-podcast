[![](https://dcbadge.limes.pink/api/server/YuMNeuKStr?style=flat)](https://discord.gg/YuMNeuKStr)
[![Docs](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/docs.yaml/badge.svg)](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/docs.yaml/)
[![Tests](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/tests.yaml/badge.svg)](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/tests.yaml/)
[![Ruff](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/lint.yaml/badge.svg?label=Ruff)](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/lint.yaml/)

<p align="center"><img src="./images/Blueprints-logo.png" width="35%" alt="Project logo"/></p>

# README-to-Podcast: Transform GitHub READMEs into Engaging Audio Explanations 🎙️

> 🔀 This is a customized fork of [mozilla-ai/document-to-podcast](https://github.com/mozilla-ai/document-to-podcast), specifically adapted to focus on explaining GitHub README files through conversational audio. While the original project handles various document types, this version is optimized for making technical documentation more accessible through audio explanations.

This blueprint demonstrates how to use open-source AI models to convert GitHub README files into engaging podcast-style conversations between a technical expert and a curious developer. Perfect for:
- 🎧 Learning about new projects while multitasking
- 📚 Making technical documentation more accessible
- 🤝 Helping newcomers understand your project
- 🌐 Breaking down complex GitHub projects into digestible discussions

### 👉 📖 For more detailed guidance on using this project, please visit our [Docs here](https://mozilla-ai.github.io/document-to-podcast/).

### Built with
- Python 3.10+ (use Python 3.12 for Apple M1/2/3 chips)
- [Llama-cpp](https://github.com/abetlen/llama-cpp-python) (text-to-text, i.e script generation)
- [OuteAI](https://github.com/edwko/OuteTTS) / [Parler_tts](https://github.com/huggingface/parler-tts) (text-to-speech, i.e audio generation)
- [Streamlit](https://streamlit.io/) (UI demo)


## Quick-start

Get started with Document-to-Podcast using one of the two options below: **GitHub Codespaces** for a hassle-free setup or **Local Installation** for running on your own machine.

---

### **Option 1: GitHub Codespaces**

The fastest way to get started. Click the button below to launch the project directly in GitHub Codespaces:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=888426876&skip_quickstart=true&machine=standardLinux32gb)

Once the Codespaces environment launches, inside the terminal, start the Streamlit demo by running:
   ```bash
   python -m streamlit run demo/app.py
   ```

### **Option 2: Local Installation**

1. **Clone the Repository**
   Inside the Codespaces terminal, run:
   ```bash
   git clone https://github.com/mozilla-ai/document-to-podcast.git
   cd document-to-podcast
   ```

2. **Install Dependencies**
   Inside the terminal, run:
   ```bash
   pip install -e .
3. **Run the Demo**
   Inside the terminal, start the Streamlit demo by running:
   ```bash
   python -m streamlit run demo/app.py
   ```

***NOTE***: The first time you run the demo app it might take a while to generate the script or the audio because it will download the models to the machine which are a few GBs in size.


## How it Works

<img src="./images/document-to-podcast-diagram.png" width="1200" />

1. **README Upload** 📄
   - Upload any GitHub README file (supports .md or .txt)


2. **Document Pre-Processing**
   The uploaded document is processed to extract and clean the text. This involves:
   - Extracting readable text from the document.
   - Removing noise such as URLs, email addresses, and special characters to ensure the text is clean and structured.

3. **Conversation Generation** 💭
   - Uses AI to transform technical content into natural dialogue
   - Features two speakers:
     - 👩‍💻 Technical Expert: Explains concepts clearly and provides implementation details
     - 🙋‍♂️ Curious Developer: Asks insightful questions and surfaces important details
   Example output:
   ```json
   {
       "Technical Expert": "Let me explain what makes this project special...",
       "Curious Developer": "That's interesting! How would someone get started with it?",
       "Technical Expert": "Great question! First, you'll need to...",
   }
   ```

4. **Audio Creation** 🎧
   - Converts the conversation into natural-sounding audio
   - Each speaker gets a distinct voice
   - Creates an engaging, podcast-style explanation

## Models

The architecture of this codebase focuses on modularity and adaptability, meaning it shouldn't be too difficult to swap frameworks to use your own suite of models. We have selected fully open source models that are very memory efficient and can run on a laptop CPU with less than 10GB RAM requirements.

### text-to-text

We are using the [llama.cpp](https://github.com/ggerganov/llama.cpp) library, which supports open source models optimized for local inference and minimal hardware requirements. The default text-to-text model in this repo is the open source [OLMoE-7B-Instruct](https://huggingface.co/allenai/OLMoE-1B-7B-0924-Instruct) from [AllenAI](https://allenai.org/).

For the complete list of models supported out-of-the-box, visit this [link](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#text-only).

### text-to-speech

We support models from the [OuteAI](https://github.com/edwko/OuteTTS) and [Parler_tts](https://github.com/huggingface/parler-tts) packages. The default text-to-speech model in this repo is [OuteTTS-0.2-500M](https://huggingface.co/OuteAI/OuteTTS-0.2-500M). Note that the `0.1-350M` version has a `CC-By-4.0` (permissive) license, whereas the newer / better `0.2-500M` version has a `CC-By-NC-4.0` (non-commercial) license.
For a complete list of models visit [Oute HF](https://huggingface.co/collections/OuteAI) (only the GGUF versions) and [Parler HF](https://huggingface.co/collections/parler-tts).

**Important note:** In order to keep the package dependencies as lightweight as possible, only the Oute interface is installed by default. If you want to use the parler models, please also follow the instructions at https://github.com/huggingface/parler-tts.

## Pre-requisites

- **System requirements**:
  - OS: Windows, macOS, or Linux
  - Python 3.10>, <3.12
  - Minimum RAM: 10 GB
  - Disk space: 32 GB minimum

- **Dependencies**:
  - Dependencies listed in `pyproject.toml`

## Troubleshooting

> When starting up the codespace, I get the message `Oh no, it looks like you are offline!`

If you are on Firefox and have Enhanced Tracking Protection `On`, try turning it `Off` for the codespace webpage.

> During the installation of the package, it fails with `ERROR: Failed building wheel for llama-cpp-python`

You are probably missing the `GNU Make` package. A quick way to solve it is run on your terminal `sudo apt install build-essential`

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
