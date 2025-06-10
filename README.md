# coqui-ai-cloning-docker
Clonning model tts_models/multilingual/multi-dataset/xtts_v2 doesn't work in docker with the typical commands. With this python code you will be able to contact the api.

```

docker run --rm -it -p 5004:5002 --gpus all --entrypoint /bin/bash ghcr.io/coqui-ai/tts
apt update
apt install nano
nano api.py (paste the code here from api.py) CTRL+X
python3 api.py
```


In your code you can call it with the parameters text and the audiofile. Deepseek is good for generating the call_coqui_tts_cloning() if you give it the api.py.

Good luck, I hope this solved your problem with cloning a voice with tts_models/multilingual/multi-dataset/xtts_v2.

