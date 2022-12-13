# sample_peyote
A multi-table synthetic data generator based on OpenAI’s GPT-3 APIs

## Todo

### Tell the story
* Write README
* Generate a bunch of files and put them on S3

### Enable low-friction replication
* Build a proper CLI
    * Add it to `scripts` in setup.py
* Add setup.py
* Add requirements.txt
* Setup testing via GH actions

### Improvements
* Bugfix: Detect failed regex matching
* Parallelize calls to create Samples