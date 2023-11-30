# Ideas
## Fine tune existing model
1. Option A: Train model here https://arxiv.org/abs/2208.08706 on new genre 
   - Propose to use this model because it is runnable and trainable on single gpu in hours
   - maybe add more tunable parameters as well 
## Fine tuning baroque counter point model, maybe RL (midi). Symbolic music generation with rule based systems (i.e. counterpoints)
## Wave, testing GAN vs diffusion (personal implementation)
1. Option A:
   - Testing GAN vs diffusion on highly compressed latent space
      - Using the autoencoder trained here: https://arxiv.org/abs/2208.08706
         - Use the autoencoder suggested here because it highly compresses the waveforms making it feasible to work on lower compute devices (ours)
      - Compare there GAN generation vs a diffusion implementation that works on the compressed latent space and is then decoded
      - Will have to create our of diffusion model
         - Maybe can find a pre trained on and re-train the input output layers (or something)



<h2>References and sources</h2>

Journal: https://transactions.ismir.net/collections/ai-and-musical-creativity

Waveform Audio Generation

https://sander.ai/2020/03/24/audio-generation.html

https://storage.googleapis.com/magentadata/papers/maestro/index.html

Models (state of the art)

MuseCoco https://ai-muzic.github.io/musecoco/

Deepbach https://github.com/Ghadjeres/DeepBach (can do both reharmonization and gnerate from scratch)

Folk rnn

MusicLM https://blog.research.google/2022/10/audiolm-language-modeling-approach-to.html

AudioLM

SingSong https://storage.googleapis.com/sing-song/index.html

Open AI Jukebox

Musenet: Similar approach to GPT-2 predict next token in a sequence.

https://magenta.tensorflow.org/piano-transformer (Transformer model)

Data sets:

https://lukewys.github.io/cocochorales/#overview (CocoChorales large dataset of generated 4 voice chorales with midi and audio)

https://magenta.tensorflow.org/datasets/maestro (Virtuoso Piano Music)