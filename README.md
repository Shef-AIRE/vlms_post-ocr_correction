## Image-Informed Post-OCR Correction with Vision-Language Models
This repository contains the code for the paper [Image-Informed Post-OCR Correction with Vision-Language Models](https://aclanthology.org/2026.findings-emnlp.60), where VLMs are adopted for post-OCR correction. We focus on post-OCR correction of historical English, using [BLN600](https://aclanthology.org/2024.lrec-main.219/), a parallel corpus of 19th century newspaper machine/human transcription.

OCR errors limit the readability and downstream NLP use of digital archives, and prior text-only correction methods overlook the visual characteristics of source documents. This work leverages the [ALTO XML schema](https://www.digitisednewspapers.net/histories/bl/) of digitised newspaper archives to create paired image, OCR text, and ground truth data for multimodal post-OCR correction. We compare Llama 3.2 Vision and Qwen 2.5-VL to their text-only LLM counterparts on BLN600, where VLMs achieve over 90% reduction in character and word error rates, showing image-informed correction is a viable, scalable approach for correcting noisy historical back catalogues.

Reproducing this pipeline from scratch requires licensed access to Gale's [British Library Newspapers](https://www.gale.com/primary-sources/british-library-newspapers): the full newspaper page scans and their word-level OCR XML are copied into `data/img` and `data/xml` respectively via `access.py`, then cropped into the paired image-patch dataset via `data.py`. To enable reproducibility, we release the image patches on Hugging Face. [`data/metadata.json`](data/metadata.json) provides document metadata, and the CSVs in [`data/`](data) provide the corresponding OCR text, ground truth, and CER/WER for each patch.

**BLN600**: https://doi.org/10.15131/shef.data.25439023  
**Image Patches**: https://huggingface.co/datasets/pykale/bln600-img-patch  
**Models**: https://huggingface.co/pykale

### Usage

Install dependencies:
```bash
pip install -r requirements.txt
```

Download the image patches from Hugging Face into `data/patch/`:
```bash
python data/download.py
```

Fine-tune a VLM using a YAML config from `config/`:
```bash
python finetune.py --config CONFIG
```

Evaluate a fine-tuned model and compute CER/WER:
```bash
python eval.py --config CONFIG
```

### Citation

```bibtex
@inproceedings{thomas-etal-2026-image,
    title = "Image-Informed Post-{OCR} Correction with Vision-Language Models",
    author = "Thomas, Alan  and
      Liu, Xianyuan  and
      Lu, Haiping  and
      Gaizauskas, Robert J.",
    editor = "Lee, Hung-Yi  and
      Dev, Sunipa  and
      Li, Jessy  and
      Elliott, Desmond",
    booktitle = "Findings of the {A}ssociation for {C}omputational {L}inguistics: {EMNLP} 2026",
    month = oct,
    year = "2026",
    address = "Budapest, Hungary",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.findings-emnlp.60/",
    pages = "1224--1237",
    ISBN = "979-8-89176-462-0",
    abstract = "Improving the quality of OCR transcriptions is crucial for researchers working with digital archives, as OCR errors hinder readability and downstream NLP tasks. While prior work has focused on seq2seq neural machine translation and, more recently, prompt-based approaches with large language models (LLMs), these methods rely solely on text, overlooking the visual characteristics of source documents. In this work, we explore the potential of vision-language models (VLMs) for post-OCR correction to evaluate the impact of integrating visual information. We conduct experiments on the BLN600 dataset of 19th-century newspaper articles, comparing Llama 3.2 Vision and Qwen 2.5 VL to their text-only LLM counterparts. Our results show that VLMs significantly outperform LLMs, achieving approximately 90{\%} reduction in character and word error rates, with the optimal setting being one that takes as input both document image and prior noisy OCR. This suggests that VLM-based post-OCR correction can be a viable and effective approach for correcting back catalogues of poorly OCR{'}ed historical documents and improving the usability of digital archives."
}
```