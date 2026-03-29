# Self-Paced Listening Experiment (PsychoPy)

## Overview

This repository contains a **self-paced listening (SPL) experiment** implemented in **PsychoPy**, together with a reproducible **Python data-cleaning pipeline** for processing the raw output generated during the experiment.

The project is designed to investigate **real-time language processing** using **segmented auditory stimuli** and **participant-controlled progression**. Participants listen to speech **segment by segment**, advancing through each trial by pressing a key, while the experiment records reaction times and final comprehension responses.

> **Important:** The **audio stimuli are not included** in this repository due to confidentiality constraints.

---

## Project Contents

This repository includes:

- **PsychoPy experiment files** (`.psyexp` and supporting code)
- **Condition files** that define the stimuli structure
- **Pseudorandomization logic** for stimulus presentation
- **Python scripts** for data cleaning and preprocessing
- An optional space for **analysis notebooks or figures**

Because the audio materials are confidential, this repository is intended to document the **experiment implementation**, the **logic of the design**, and the **processing workflow**, rather than to distribute the full stimulus set.

---

## Experiment Design

### Self-Paced Listening Paradigm

In this experiment, participants hear auditory materials in a **self-paced** format. Instead of hearing the full sentence continuously, they advance through the stimulus **one segment at a time**, allowing the researcher to capture timing differences associated with online processing.

Each trial typically consists of the following sequence:

1. **Audio segment playback**
2. **Participant key press to continue**
3. **Reaction time recording**
4. **Final comprehension question**
5. **Response collection** (for example, using `F` / `J` keys)

This paradigm makes it possible to examine how processing difficulty may vary across segments and experimental conditions.

---

### Stimuli and Conditions

The experiment uses **pre-segmented audio stimuli**, but those files are **not distributed** in this repository.

The condition files (`.csv`) define the structure of the experiment, such as:

- `item_id`
- condition type
- segment order
- question information
- references to the corresponding audio files

Since the audio files are confidential, anyone reusing this code will need to:

- provide their **own audio stimuli**
- make sure the **file paths** in the condition files are valid
- preserve the same expected structure used by the PsychoPy experiment

---

### Pseudorandomization

The experiment uses a **custom pseudorandomization procedure** to control the order of item presentation.

The goal of this procedure is to avoid undesirable repetition patterns while maintaining a balanced distribution of conditions. In particular, the randomization logic is designed so that:

- no more than **two items of the same condition** appear consecutively
- experimental conditions remain reasonably balanced across the session

This step is important for reducing order effects and improving the quality of the resulting data.

---

## Running the Experiment

### Requirements

To run the experiment, you will need:

- **Python 3.12**
- **PsychoPy**

## Setup

1. Open the `.psyexp` file in **PsychoPy Builder**
2. Locate the condition files (`.csv`)
3. Update all audio file paths to your local (confidential) stimuli
4. Verify that folder paths match your local setup
5. Run the experiment from PsychoPy

---

## Data Output

Running the experiment will generate raw files such as:

- `.csv` (primary data file)  
- `.psydat` (PsychoPy internal format)  

These files include:

- Trial-level information  
- Segment-level reaction times  
- Key responses (e.g., F/J)  
- PsychoPy metadata and timestamps  

---

## Data Cleaning Pipeline

The cleaning script is located in:

```bash
scripts/clean_data.py
```
### Purpose

The script:

- Removes unnecessary PsychoPy metadata  
- Aligns reaction times with experimental items  
- Extracts comprehension responses  
- Produces a cleaner dataset for analysis  

---

## Analysis

Optional analysis scripts or notebooks can be added for:

- Reaction time distributions  
- Condition comparisons  
- Statistical modeling  

---

## Notes

- Audio files are not included due to confidentiality  
- You must provide your own stimuli  
- File paths will need to be updated before running  
- Raw experimental data should not be publicly shared if sensitive  

---

## Dependencies

Main dependencies:

- PsychoPy  
- pandas  
- numpy
  
## Author
Davo Acevedo-Cardona
MS in Human Language Technology
University of Arizona
