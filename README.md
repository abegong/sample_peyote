# sample_peyote
A multi-table synthetic data generator based on OpenAI’s GPT-3 APIs

## Overview

This project is an experiment in LLM-based workflows. Functionally, my goal is to be able to quickly create semi-realistic synthetic data.

I want to be able to...

* Start from scratch: Most synthetic data generators work by taking a sample of real data, and generating a fake dataset that has similar properties. I want to generate (aka "hallucinate") data starting from just an idea.
* Cover any topic: I want to be able to generate data related to many different topics.
* Generate a database, not just a table: I don't just want to generate a table. I want to generate a realistic-feeling database, with multiple tables and realistic use of things like foreign keys, ENUMs, and timestamps.

## What's good enough?
At the end of the day, I want to generate data that "feels authentic." This is squishy, but [sometimes that's what it comes down to](https://en.wikipedia.org/wiki/I_know_it_when_I_see_it) when we're evaluating content.

Here's my litmus test: Let's say you're watching a Hollywood blockbuster including some kind of data-related MacGuffin. There's a tense scene where the characters are looking at a screen: "Oh no! The Jackal is hacking the power grid database!" or "Captain, we've unencrypted the alien message. It's a SQLITE database." You freeze playback, and output from Sample Peyote appears on the screen.

If you showed the screen to a professional data analyst/scientist/engineer, would they [cringe](https://www.reddit.com/r/programming/comments/76c2e/whats_the_worst_it_reference_youve_seen_in_a/)? Or look thoughtful and say, "hey, that's actually pretty good!"

That's the bar.

## What's with the name?
Well, it helps you [hallucinate](https://arxiv.org/abs/2202.03629) data samples.

## Installation and usage

Installation
```
git clone git@github.com:abegong/sample_peyote.git
cd sample_peyote
pip install .
```

You'll also need to have a valid `OPENAI_API_KEY` configured in your environment variables.

:warning: RUNNING SAMPLE PEYOTE COSTS MONEY. Each run of Sample Peyote costs about $0.05 worth of OpenAI credits. That's based refreshing my Billing page and eyeballing how much the Usage bar increased over the course of a couple hours of experimentation, so if you're going to scale this up and spend significant money, you'll want to do your own (better) estimation.

Basic usage:
```
sample_peyote
```

Sample Peyote will
1. ask you for a topic,
2. generate some ideas for you,
3. ask you to choose one of the ideas,
4. generate tables and samples for you.

You can specify a topic to skip step 1: `sample_peyote --topic quadrilaterals`

For multi-word topics, please use quotes:  `sample_peyote --topic "The Beatles"`

If you specify `-n 1` (only generate a single idea), it'll skip step 3: `sample_peyote -n 1`

If you specify `--silent` or `-s`, it will suppress print output. Combined with the other a topic and `-n 1`, this allows headless generation of datasets: `sample_peyote --topic "The Beatles" -n 1 --silent`

## Output

On each run, Schema Peyote will generate a directory that looks like this:

```
├── dataset_ideas.json
├── summary-beatles-song-lyrics-data.md
├── tables-beatles-song-lyrics-data.jl
└── samples                                 # Contains the data samples themselves
    ├── albums.csv
    ├── artists.csv
    ├── genres.csv
    ├── performances.csv
    ├── song-lyrics.csv
    ├── tracks.csv
    └── writers.csv
```

## Known issues

This program relies on regex parsing of replies from OpenAI's Davinci text model. I've done some basic prompt engineering to make Davinci more likely to return well-formatted responses, but it's not perfect. I'd guess that it fails about 10% of the time, but that's not based on anything scientific. 

Since I'm only using this for demo purposes, that's good enough that I haven't bothered to trap, log, and set up retry logic for those errors. If you were going to use Sample Peyote for real, you'd want to make it more reliable. (:merge: PRs welcome!)

## Why synthetic data?

Use of synthetic data is on the rise, to boost the size of training sets for ML models, and to test algorithms and data systems with less risk of exposing sensitive data. I also have a hunch that sufficiently realistic datasets could be useful for classes and bootcamps for data scientists and engineers. [It's hard to find realistic datasets without working within a real organization](https://analyticsengineers.club/data-education-is-broken/).

In other words, there's a possiblity that Sample Peyote might actually be useful to somebody. If that somebody is you, please have at it! I've open sourced Sample Peyote under the Apache 2.0 license. I'm also happy to accept PRs, but please don't expect quick turnaround---I'm not planning to invest a ton of time in this project.

### My real goal

My real goal for this project was to explore how AI-based workflows are likely to evolve in the future. As a data guy and entrepreneur, my interest naturally gravitated in that direction. I built the core of Schema Peyote in a weekend, then spent a few more hours packaging it up to share via Github.

I'm very bullish on the potential for AI-based tools to unlock a lot ton of productivity and creativity, but I also believe that they're going to cause sweeping changes that we aren't ready for as a society. I'm also doing a lot of thinking about how those changes are going to play out within the world of data, analytics, and epistemology (i.e. "learning and reasoning together based on evidence.")

If this stuff interests you too, please reach out! As of Dec 2022, I'm active on twitter under the handle [@abegong](https://twitter.com/AbeGong).

## Todo

### Tell the story
* Generate a bunch of files and put them on S3

### Improvements
* Setup testing via GH actions
* Bugfix: Detect failed regex matching
* Add better error trapping in general
* Add logging
* Parallelize API calls to create Samples, for faster execution
