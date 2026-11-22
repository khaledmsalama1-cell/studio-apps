#!/usr/bin/env python3
"""Seed data for the studio-apps registry. Writes apps/<id>.json (one file per app).

Run once to (re)generate the entry files, then `node scripts/build-index.mjs`.
After the first seed, edit the JSON files directly; this script is kept as a record.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def link():
    return {"type": "link"}

def keys(*k):
    return {"type": "keys", "keys": list(k)}

def folder():
    return {"type": "folder"}

def skills(repo):
    return {"type": "skills-repo", "repo": repo}

def mcp_http(name, url, key=None, oauth=False):
    cfg = {"type": "http", "url": url}
    if key:
        cfg["headers"] = {"Authorization": "Bearer ${%s}" % key}
    out = {"type": "mcp", "name": name, "config": cfg, "keys": [key] if key else []}
    if oauth:
        out["oauth"] = True
    return out

def mcp_cmd(name, cmd, args, *envkeys):
    cfg = {"command": cmd, "args": args}
    if envkeys:
        cfg["env"] = {k: "${%s}" % k for k in envkeys}
    return {"type": "mcp", "name": name, "config": cfg, "keys": list(envkeys)}

APPS = []

def A(id, name, category, kind, pricing, tagline, description, links, license=None, integration=None, tags=(), color=None):
    APPS.append({
        "id": id, "name": name, "category": category, "kind": kind, "pricing": pricing,
        **({"license": license} if license else {}),
        "tagline": tagline, "description": description, "links": links,
        "integration": integration or link(), "tags": list(tags),
        **({"color": color} if color else {}),
    })

gh = lambda r: {"GitHub": f"https://github.com/{r}"}

# ---------------------------------------------------------------- video engines
A("hyperframes", "HyperFrames", "video-engines", "open-source", "free", "Write HTML, render MP4", "HTML + GSAP compositions rendered to video by agents. The Studio's default engine.", {"Website": "https://hyperframes.heygen.com", **gh("heygen-com/hyperframes")}, "Apache-2.0", tags=["video", "html", "gsap"], color="#2747E8")
A("remotion", "Remotion", "video-engines", "open-source", "freemium", "Videos as React components", "Programmatic video with React. Free for individuals and small companies; company license above that.", {"Website": "https://www.remotion.dev", **gh("remotion-dev/remotion")}, "Remotion License", tags=["video", "react"], color="#0B84F3")
A("motion-canvas", "Motion Canvas", "video-engines", "open-source", "free", "Animations written in TypeScript", "A TypeScript library and editor for explainer-style animations, synced to voiceover.", {"Website": "https://motioncanvas.io", **gh("motion-canvas/motion-canvas")}, "MIT", tags=["animation", "typescript"], color="#33A6FF")
A("revideo", "Revideo", "video-engines", "open-source", "free", "Motion Canvas, built for rendering at scale", "A fork of Motion Canvas focused on programmatic rendering through an API.", {"Website": "https://re.video", **gh("redotvideo/revideo")}, "MIT", tags=["video", "typescript"], color="#5B5BD6")
A("manim", "Manim", "video-engines", "open-source", "free", "Math and diagram animations in Python", "The community edition of the animation engine behind explainer channels like 3Blue1Brown.", {"Website": "https://www.manim.community", **gh("ManimCommunity/manim")}, "MIT", tags=["animation", "python", "explainer"], color="#2A6F97")
A("ffmpeg", "FFmpeg", "video-engines", "open-source", "free", "The video toolbox under everything", "Convert, cut, crop, resize and mix audio and video from the command line.", {"Website": "https://ffmpeg.org"}, "LGPL/GPL", tags=["cli", "video", "audio"], color="#2C8C3C")
A("blender", "Blender", "video-engines", "open-source", "free", "3D, motion graphics and video editing", "Free 3D suite with a video sequencer; scriptable with Python for product renders.", {"Website": "https://www.blender.org"}, "GPL", integration=folder(), tags=["3d", "desktop"], color="#E87D0D")

# ---------------------------------------------------------------- editors
A("kdenlive", "Kdenlive", "editors", "open-source", "free", "Full non-linear video editor", "A free multi-track editor for Linux, Windows and macOS.", {"Website": "https://kdenlive.org"}, "GPL", integration=folder(), tags=["desktop", "editing"], color="#1F6FB2")
A("shotcut", "Shotcut", "editors", "open-source", "free", "Cross-platform video editor", "A free editor with wide format support and no import step.", {"Website": "https://shotcut.org", **gh("mltframework/shotcut")}, "GPL", integration=folder(), tags=["desktop", "editing"], color="#2B7A0B")
A("openshot", "OpenShot", "editors", "open-source", "free", "Simple video editor", "Beginner-friendly editor with titles, transitions and keyframes.", {"Website": "https://www.openshot.org", **gh("OpenShot/openshot-qt")}, "GPL", integration=folder(), tags=["desktop", "editing"], color="#C0392B")
A("obs", "OBS Studio", "editors", "open-source", "free", "Record and stream your screen and camera", "Record talking-head footage and screen demos to use as media scenes.", {"Website": "https://obsproject.com", **gh("obsproject/obs-studio")}, "GPL", integration=folder(), tags=["recording", "desktop"], color="#302E31")
A("davinci-resolve", "DaVinci Resolve", "editors", "desktop", "freemium", "Pro editing, color and audio", "Free version covers editing, color grading and Fairlight audio; Studio version is paid.", {"Website": "https://www.blackmagicdesign.com/products/davinciresolve"}, integration=folder(), tags=["desktop", "editing", "color"], color="#1B1B1B")
A("capcut", "CapCut", "editors", "service", "freemium", "Mobile-first editor with templates", "Popular editor for short-form video with trend templates and auto-captions.", {"Website": "https://www.capcut.com"}, integration=folder(), tags=["short-form", "editing"], color="#000000")
A("descript", "Descript", "editors", "service", "freemium", "Edit video by editing the transcript", "Text-based editing, filler-word removal, overdub and studio sound.", {"Website": "https://www.descript.com"}, integration=folder(), tags=["editing", "podcast"], color="#1C1C1C")
A("auto-editor", "auto-editor", "editors", "open-source", "free", "Cut silences automatically", "Command-line tool that removes dead air from talking-head footage.", {**gh("WyattBlue/auto-editor")}, "Unlicense", tags=["cli", "editing"], color="#3B3B98")
A("opus-clip", "Opus Clip", "editors", "service", "freemium", "Long video into viral shorts", "Finds the best moments in long videos and reframes them to vertical clips.", {"Website": "https://www.opus.pro"}, integration=folder(), tags=["repurpose", "short-form"], color="#5E3BEE")
A("submagic", "Submagic", "editors", "service", "paid", "Animated captions for shorts", "Auto-captions, emojis and b-roll for short-form video.", {"Website": "https://www.submagic.co"}, integration=folder(), tags=["captions", "short-form"], color="#6C5CE7")

# ---------------------------------------------------------------- motion
A("gsap", "GSAP", "motion", "open-source", "free", "The animation library HyperFrames uses", "Professional JavaScript animation library, free for all uses since 2025.", {"Website": "https://gsap.com", **gh("greensock/GSAP")}, tags=["javascript", "animation"], color="#0AE448")
A("lottie", "Lottie", "motion", "open-source", "free", "Lightweight vector animations", "Render After Effects animations exported as JSON on web and mobile.", {"Website": "https://airbnb.io/lottie", **gh("airbnb/lottie-web")}, "MIT", tags=["animation", "vector"], color="#00DDB3")
A("lottiefiles", "LottieFiles", "motion", "service", "freemium", "Library of ready Lottie animations", "Thousands of free animations and an editor for Lottie files.", {"Website": "https://lottiefiles.com"}, tags=["animation", "assets"], color="#00C1A2")
A("rive", "Rive", "motion", "service", "freemium", "Interactive animations with state machines", "Design and ship interactive vector animations.", {"Website": "https://rive.app"}, tags=["animation", "interactive"], color="#1D1D1D")
A("theatre-js", "Theatre.js", "motion", "open-source", "free", "Motion design editor for the web", "A timeline editor for animating web and Three.js scenes in the browser.", {"Website": "https://www.theatrejs.com", **gh("theatre-js/theatre")}, "Apache-2.0", tags=["animation", "3d"], color="#E2475C")
A("threejs", "Three.js", "motion", "open-source", "free", "3D in the browser", "The standard WebGL library; works inside HyperFrames and Remotion compositions.", {"Website": "https://threejs.org", **gh("mrdoob/three.js")}, "MIT", tags=["3d", "webgl"], color="#049EF4")

# ---------------------------------------------------------------- voice & TTS
A("elevenlabs", "ElevenLabs", "voice", "service", "freemium", "The voices people can't tell from real", "Text to speech with timings, voice design and cloning, music and sound effects. Official hosted MCP server (sign in once); the API key powers the Studio's voiceover script.", {"Website": "https://elevenlabs.io", "MCP docs": "https://elevenlabs.io/docs/agents-platform/operate/hosted-mcp"}, integration={**mcp_http("elevenlabs", "https://api.elevenlabs.io/v1/mcp", oauth=True), "keys": ["ELEVENLABS_API_KEY"]}, tags=["tts", "cloning", "music"], color="#111111")
A("kokoro", "Kokoro", "voice", "open-source", "free", "Small, fast, free local TTS", "An 82M-parameter model with natural English voices that runs on a laptop.", {"Model": "https://huggingface.co/hexgrad/Kokoro-82M", **gh("hexgrad/kokoro")}, "Apache-2.0", tags=["tts", "local"], color="#E86A33")
A("chatterbox", "Chatterbox", "voice", "open-source", "free", "Expressive open TTS with cloning", "Resemble AI's MIT-licensed TTS family with emotion control and 23+ languages.", {**gh("resemble-ai/chatterbox")}, "MIT", tags=["tts", "cloning", "local"], color="#C2410C")
A("piper", "Piper", "voice", "open-source", "free", "Fast offline TTS for many languages", "Lightweight neural TTS that runs on CPU, with voices in dozens of languages.", {**gh("OHF-Voice/piper1-gpl")}, "GPL-3.0", tags=["tts", "local", "multilingual"], color="#3A7D44")
A("f5-tts", "F5-TTS", "voice", "open-source", "free", "Zero-shot voice cloning TTS", "Research TTS that clones a voice from a short reference clip.", {**gh("SWivid/F5-TTS")}, "MIT (code)", tags=["tts", "cloning", "local"], color="#7B3FE4")
A("fish-speech", "Fish Speech / OpenAudio", "voice", "open-source", "freemium", "Multilingual TTS and cloning", "Open models plus a hosted API from Fish Audio.", {"Website": "https://fish.audio", **gh("fishaudio/fish-speech")}, tags=["tts", "cloning"], color="#1E88E5")
A("coqui-tts", "Coqui TTS", "voice", "open-source", "free", "Toolkit with XTTS and many models", "Python toolkit for training and running TTS models, including XTTS v2.", {**gh("coqui-ai/TTS")}, "MPL-2.0", tags=["tts", "local"], color="#4B9CD3")
A("bark", "Bark", "voice", "open-source", "free", "Text to audio with laughs and music", "Generates speech with non-verbal sounds like laughing and sighing.", {**gh("suno-ai/bark")}, "MIT", tags=["tts", "local"], color="#8B5E34")
A("dia", "Dia", "voice", "open-source", "free", "Realistic two-speaker dialogue", "Generates natural dialogue between speakers from a script.", {**gh("nari-labs/dia")}, "Apache-2.0", tags=["tts", "dialogue"], color="#D35400")
A("orpheus-tts", "Orpheus TTS", "voice", "open-source", "free", "Human-sounding open TTS", "LLM-based speech model with emotive tags.", {**gh("canopyai/Orpheus-TTS")}, "Apache-2.0", tags=["tts", "local"], color="#6D28D9")
A("sesame-csm", "Sesame CSM", "voice", "open-source", "free", "Conversational speech model", "Generates conversational speech from text and audio context.", {**gh("SesameAILabs/csm")}, "Apache-2.0", tags=["tts", "conversational"], color="#B45309")
A("styletts2", "StyleTTS 2", "voice", "open-source", "free", "Human-level TTS research model", "Style diffusion TTS trained on LJSpeech and LibriTTS.", {**gh("yl4579/StyleTTS2")}, "MIT", tags=["tts", "research"], color="#0F766E")
A("cartesia", "Cartesia", "voice", "service", "paid", "Ultra-low-latency voice API", "Fast, expressive TTS API with voice cloning.", {"Website": "https://cartesia.ai"}, integration=keys("CARTESIA_API_KEY"), tags=["tts", "api"], color="#2D2D2D")
A("openai-tts", "OpenAI TTS", "voice", "service", "paid", "Speech from the OpenAI API", "Text-to-speech voices available through the OpenAI audio API.", {"Docs": "https://platform.openai.com/docs/guides/text-to-speech"}, integration=keys("OPENAI_API_KEY"), tags=["tts", "api"], color="#10A37F")
A("voicebox", "Voicebox", "voice", "open-source", "free", "An open-source voice studio", "Local desktop app for cloning and TTS with several engines and 23 languages. Connect its export folder.", {**gh("jamiepine/voicebox")}, "MIT", integration=folder(), tags=["desktop", "tts", "cloning"], color="#5B4BDB")

# ---------------------------------------------------------------- voice cloning / conversion
A("rvc", "RVC", "voice-clone", "open-source", "free", "Retrieval-based voice conversion", "Train a voice model and convert recordings into that voice.", {**gh("RVC-Project/Retrieval-based-Voice-Conversion-WebUI")}, "MIT", tags=["conversion", "local"], color="#7C3AED")
A("applio", "Applio", "voice-clone", "open-source", "free", "Friendly voice conversion app", "A polished RVC-based app for training and converting voices.", {"Website": "https://applio.org", **gh("IAHispano/Applio")}, "MIT", integration=folder(), tags=["conversion", "desktop"], color="#16A34A")
A("openvoice", "OpenVoice", "voice-clone", "open-source", "free", "Instant voice cloning", "Clone a voice's tone color and speak in multiple languages.", {**gh("myshell-ai/OpenVoice")}, "MIT", tags=["cloning", "local"], color="#0EA5E9")

# ---------------------------------------------------------------- transcription
A("whisper", "Whisper", "transcription", "open-source", "free", "Speech recognition in 99 languages", "OpenAI's open speech model; HyperFrames uses it for caption timings.", {**gh("openai/whisper")}, "MIT", tags=["asr", "local"], color="#10A37F")
A("whisper-cpp", "whisper.cpp", "transcription", "open-source", "free", "Whisper in fast C/C++", "Runs Whisper efficiently on CPU and Apple Silicon.", {**gh("ggml-org/whisper.cpp")}, "MIT", tags=["asr", "local"], color="#444444")
A("faster-whisper", "faster-whisper", "transcription", "open-source", "free", "Up to 4x faster Whisper", "CTranslate2 reimplementation of Whisper with word timestamps.", {**gh("SYSTRAN/faster-whisper")}, "MIT", tags=["asr", "python"], color="#2563EB")
A("whisperx", "WhisperX", "transcription", "open-source", "free", "Word-level timestamps and speakers", "Whisper with forced alignment and speaker diarization.", {**gh("m-bain/whisperX")}, "BSD-2", tags=["asr", "diarization"], color="#1D4ED8")
A("parakeet", "NVIDIA Parakeet", "transcription", "open-source", "free", "Fast, accurate English ASR", "NVIDIA NeMo speech models; HyperFrames can use Parakeet for captions.", {**gh("NVIDIA/NeMo")}, "Apache-2.0", tags=["asr", "local"], color="#76B900")
A("deepgram", "Deepgram", "transcription", "service", "freemium", "Speech-to-text API", "Fast transcription with diarization and smart formatting.", {"Website": "https://deepgram.com"}, integration=keys("DEEPGRAM_API_KEY"), tags=["asr", "api"], color="#13EF93")
A("assemblyai", "AssemblyAI", "transcription", "service", "freemium", "Speech AI models via API", "Transcription with speaker labels, summaries and chapters.", {"Website": "https://www.assemblyai.com"}, integration=keys("ASSEMBLYAI_API_KEY"), tags=["asr", "api"], color="#2545D3")

# ---------------------------------------------------------------- music & sound
A("suno", "Suno", "music", "service", "freemium", "Songs from a prompt", "Generates full songs with vocals; check its terms for commercial use.", {"Website": "https://suno.com"}, integration=folder(), tags=["music", "generation"], color="#000000")
A("udio", "Udio", "music", "service", "freemium", "AI music generation", "Generate and extend tracks in many genres.", {"Website": "https://www.udio.com"}, integration=folder(), tags=["music", "generation"], color="#E11D48")
A("audiocraft", "AudioCraft (MusicGen)", "music", "open-source", "free", "Meta's open music and audio models", "MusicGen and AudioGen for music and sound effects from text.", {**gh("facebookresearch/audiocraft")}, "MIT (code)", tags=["music", "sfx", "local"], color="#0866FF")
A("stable-audio-open", "Stable Audio Open", "music", "open-source", "free", "Open text-to-audio model", "Stability AI's model for sound effects and short music clips.", {**gh("Stability-AI/stable-audio-tools")}, tags=["sfx", "music", "local"], color="#7C3AED")
A("ace-step", "ACE-Step", "music", "open-source", "free", "Open music foundation model", "Fast open-source song generation with lyrics.", {**gh("ace-step/ACE-Step")}, "Apache-2.0", tags=["music", "local"], color="#F97316")
A("yue", "YuE", "music", "open-source", "free", "Open full-song generation", "Generates songs with vocals from lyrics.", {**gh("multimodal-art-projection/YuE")}, "Apache-2.0", tags=["music", "local"], color="#9333EA")
A("freesound", "Freesound", "music", "service", "free", "Creative Commons sound effects", "Huge library of user-uploaded sounds; check each license.", {"Website": "https://freesound.org"}, integration=keys("FREESOUND_API_KEY"), tags=["sfx", "stock"], color="#E52E2E")
A("epidemic-sound", "Epidemic Sound", "music", "service", "paid", "Licensed music for social", "Subscription library cleared for social platforms.", {"Website": "https://www.epidemicsound.com"}, integration=folder(), tags=["music", "stock"], color="#111111")
A("artlist", "Artlist", "music", "service", "paid", "Music, SFX and footage license", "Royalty-free music, sound effects and stock footage.", {"Website": "https://artlist.io"}, integration=folder(), tags=["music", "stock"], color="#FFCD00")
A("youtube-audio-library", "YouTube Audio Library", "music", "service", "free", "Free music for YouTube", "Free tracks and effects inside YouTube Studio; check attribution rules.", {"Website": "https://studio.youtube.com"}, integration=folder(), tags=["music", "free"], color="#FF0000")

# ---------------------------------------------------------------- audio cleanup
A("demucs", "Demucs", "audio-tools", "open-source", "free", "Separate vocals, drums and bass", "Music source separation; pull a clean voice out of a noisy clip.", {**gh("adefossez/demucs")}, "MIT", tags=["separation", "local"], color="#0866FF")
A("uvr", "Ultimate Vocal Remover", "audio-tools", "open-source", "free", "Vocal removal desktop app", "GUI for vocal and instrument separation models.", {**gh("Anjok07/ultimatevocalremovergui")}, "MIT", integration=folder(), tags=["separation", "desktop"], color="#DC2626")
A("audacity", "Audacity", "audio-tools", "open-source", "free", "Record and edit audio", "Free multi-track audio editor for cleaning up voiceovers.", {"Website": "https://www.audacityteam.org", **gh("audacity/audacity")}, "GPL", integration=folder(), tags=["audio", "desktop"], color="#0000CC")
A("adobe-podcast", "Adobe Podcast Enhance", "audio-tools", "service", "freemium", "Make any recording sound studio-made", "Web tool that removes noise and echo from speech.", {"Website": "https://podcast.adobe.com/enhance"}, integration=folder(), tags=["cleanup", "speech"], color="#EB1000")

# ---------------------------------------------------------------- image generation
A("flux", "FLUX", "image-gen", "open-source", "freemium", "State-of-the-art image models", "Black Forest Labs' image models; open weights for dev/schnell and an API.", {"Website": "https://bfl.ai", **gh("black-forest-labs/flux")}, tags=["image", "local", "api"], color="#111111")
A("comfyui", "ComfyUI", "image-gen", "open-source", "free", "Node-based image and video generation", "The most flexible local UI for diffusion workflows.", {"Website": "https://www.comfy.org", **gh("comfyanonymous/ComfyUI")}, "GPL", integration=folder(), tags=["image", "video", "local"], color="#172DD7")
A("automatic1111", "Stable Diffusion WebUI", "image-gen", "open-source", "free", "The classic Stable Diffusion UI", "AUTOMATIC1111's web UI with a huge extension ecosystem.", {**gh("AUTOMATIC1111/stable-diffusion-webui")}, "AGPL", integration=folder(), tags=["image", "local"], color="#F97316")
A("fooocus", "Fooocus", "image-gen", "open-source", "free", "Prompt-first image generation", "Simple local image generation with good defaults.", {**gh("lllyasviel/Fooocus")}, "GPL", integration=folder(), tags=["image", "local"], color="#22C55E")
A("invokeai", "InvokeAI", "image-gen", "open-source", "free", "Creative studio for diffusion models", "Canvas-based image generation for professional workflows.", {"Website": "https://invoke.com", **gh("invoke-ai/InvokeAI")}, "Apache-2.0", integration=folder(), tags=["image", "local"], color="#E9B53B")
A("midjourney", "Midjourney", "image-gen", "service", "paid", "Distinctive image generation", "Popular image model with strong aesthetics; web and Discord.", {"Website": "https://www.midjourney.com"}, integration=folder(), tags=["image"], color="#000000")
A("ideogram", "Ideogram", "image-gen", "service", "freemium", "Images with readable text", "Strong at typography and posters.", {"Website": "https://ideogram.ai"}, integration=folder(), tags=["image", "typography"], color="#1F1F1F")
A("recraft", "Recraft", "image-gen", "service", "freemium", "Brand-consistent images and vectors", "Generates SVG vectors, icons and on-brand illustrations.", {"Website": "https://www.recraft.ai"}, integration=keys("RECRAFT_API_TOKEN"), tags=["image", "vector", "brand"], color="#0D0D0D")
A("leonardo", "Leonardo.Ai", "image-gen", "service", "freemium", "Image and video generation suite", "Image models, canvas editing and motion for creators.", {"Website": "https://leonardo.ai"}, integration=keys("LEONARDO_API_KEY"), tags=["image", "video"], color="#6B21A8")
A("krea", "Krea", "image-gen", "service", "freemium", "Real-time generation and enhancing", "Real-time image generation, upscaling and video.", {"Website": "https://www.krea.ai"}, integration=folder(), tags=["image", "upscale"], color="#000000")
A("gemini-image", "Gemini image (Imagen)", "image-gen", "service", "paid", "Google's image generation and editing", "Image generation and conversational editing through the Gemini API.", {"Docs": "https://ai.google.dev/gemini-api/docs/image-generation"}, integration=keys("GEMINI_API_KEY"), tags=["image", "api"], color="#4285F4")
A("openai-images", "OpenAI Images", "image-gen", "service", "paid", "Image generation from the OpenAI API", "Generate and edit images with OpenAI's image models.", {"Docs": "https://platform.openai.com/docs/guides/image-generation"}, integration=keys("OPENAI_API_KEY"), tags=["image", "api"], color="#10A37F")

# ---------------------------------------------------------------- video generation
A("fal", "fal", "video-gen", "service", "paid", "1,000+ image, video and audio models", "One API for Flux, Veo, Kling and more. Official MCP server.", {"Website": "https://fal.ai", "MCP docs": "https://fal.ai/docs/documentation/setting-up/mcp"}, integration=mcp_http("fal", "https://mcp.fal.ai/mcp", "FAL_KEY"), tags=["image", "video", "api"], color="#7A3CE0")
A("replicate", "Replicate", "video-gen", "service", "paid", "Run open models in the cloud", "Thousands of models through one API. Official MCP server.", {"Website": "https://replicate.com", "MCP": "https://mcp.replicate.com"}, integration=mcp_cmd("replicate", "npx", ["-y", "replicate-mcp"], "REPLICATE_API_TOKEN"), tags=["image", "video", "api"], color="#E2513C")
A("runway", "Runway", "video-gen", "service", "paid", "Gen video models and editing tools", "Text and image to video, plus AI editing tools and an API.", {"Website": "https://runwayml.com"}, integration=keys("RUNWAYML_API_SECRET"), tags=["video", "api"], color="#000000")
A("luma", "Luma Dream Machine", "video-gen", "service", "freemium", "Cinematic video from text and images", "Video generation with camera control; API available.", {"Website": "https://lumalabs.ai"}, integration=keys("LUMAAI_API_KEY"), tags=["video", "api"], color="#1A1A1A")
A("kling", "Kling", "video-gen", "service", "freemium", "High-motion video generation", "Kuaishou's video models, also available through fal and Replicate.", {"Website": "https://klingai.com"}, integration=folder(), tags=["video"], color="#0A0A0A")
A("veo", "Google Veo", "video-gen", "service", "paid", "Google's video model with audio", "Video generation with native sound via the Gemini API and Vertex AI.", {"Docs": "https://ai.google.dev/gemini-api/docs/video"}, integration=keys("GEMINI_API_KEY"), tags=["video", "api"], color="#4285F4")
A("pika", "Pika", "video-gen", "service", "freemium", "Playful video effects and generation", "Short video generation and effects for social.", {"Website": "https://pika.art"}, integration=folder(), tags=["video", "effects"], color="#111111")
A("minimax-hailuo", "MiniMax Hailuo", "video-gen", "service", "freemium", "Video generation with strong motion", "Hailuo video models from MiniMax.", {"Website": "https://hailuoai.video"}, integration=folder(), tags=["video"], color="#E63946")
A("higgsfield", "Higgsfield", "video-gen", "service", "paid", "Camera-motion presets for AI video", "Cinematic camera moves and effects for generated video.", {"Website": "https://higgsfield.ai"}, integration=folder(), tags=["video", "effects"], color="#1C1C1C")
A("wan", "Wan", "video-gen", "open-source", "free", "Open video generation models", "Alibaba's open text-to-video and image-to-video models.", {**gh("Wan-Video/Wan2.1")}, "Apache-2.0", tags=["video", "local"], color="#FF6A00")
A("hunyuan-video", "HunyuanVideo", "video-gen", "open-source", "free", "Tencent's open video model", "Large open-weights text-to-video model.", {**gh("Tencent/HunyuanVideo")}, tags=["video", "local"], color="#0052D9")
A("ltx-video", "LTX-Video", "video-gen", "open-source", "free", "Fast open video generation", "Lightricks' real-time-capable open video model.", {**gh("Lightricks/LTX-Video")}, tags=["video", "local"], color="#2D2D2D")
A("cogvideo", "CogVideoX", "video-gen", "open-source", "free", "Open text-to-video model", "Open video generation from the GLM team.", {**gh("THUDM/CogVideo")}, "Apache-2.0", tags=["video", "local"], color="#3B82F6")
A("mochi", "Mochi", "video-gen", "open-source", "free", "Open video model from Genmo", "Apache-licensed text-to-video model.", {**gh("genmoai/mochi")}, "Apache-2.0", tags=["video", "local"], color="#F59E0B")

# ---------------------------------------------------------------- avatars & lip-sync
A("heygen", "HeyGen", "avatars", "service", "paid", "AI avatars that present for you", "Avatar videos and translation; official MCP server with browser sign-in.", {"Website": "https://www.heygen.com", "MCP docs": "https://developers.heygen.com/mcp/claude-code"}, integration=mcp_http("heygen", "https://mcp.heygen.com/mcp/v1/", oauth=True), tags=["avatar", "video"], color="#1F6FEB")
A("synthesia", "Synthesia", "avatars", "service", "paid", "Avatar videos for business", "Studio-quality AI presenters in 140+ languages.", {"Website": "https://www.synthesia.io"}, integration=folder(), tags=["avatar", "video"], color="#2F1C6A")
A("d-id", "D-ID", "avatars", "service", "paid", "Talking photos and agents", "Animate a portrait into a speaking video; API available.", {"Website": "https://www.d-id.com"}, integration=keys("DID_API_KEY"), tags=["avatar", "api"], color="#00C2FF")
A("liveportrait", "LivePortrait", "avatars", "open-source", "free", "Animate a portrait from a driving video", "Efficient open portrait animation.", {**gh("KwaiVGI/LivePortrait")}, "MIT", tags=["avatar", "local"], color="#EC4899")
A("sadtalker", "SadTalker", "avatars", "open-source", "free", "Talking head from one image and audio", "Generates a talking-head video from a photo and a voiceover.", {**gh("OpenTalker/SadTalker")}, "Apache-2.0", tags=["avatar", "local"], color="#8B5CF6")
A("wav2lip", "Wav2Lip", "avatars", "open-source", "free", "Lip-sync any video to audio", "Classic lip-sync model (research/non-commercial license).", {**gh("Rudrabha/Wav2Lip")}, tags=["lip-sync", "local"], color="#6366F1")
A("latentsync", "LatentSync", "avatars", "open-source", "free", "High-quality open lip-sync", "ByteDance's diffusion-based lip-sync model.", {**gh("bytedance/LatentSync")}, "Apache-2.0", tags=["lip-sync", "local"], color="#0EA5E9")

# ---------------------------------------------------------------- image tools
A("rembg", "rembg", "image-tools", "open-source", "free", "Remove image backgrounds", "Command-line and Python background removal for product shots.", {**gh("danielgatis/rembg")}, "MIT", tags=["cutout", "local"], color="#0F172A")
A("birefnet", "BiRefNet", "image-tools", "open-source", "free", "Precise background removal", "High-resolution dichotomous segmentation for clean cutouts.", {**gh("ZhengPeng7/BiRefNet")}, "MIT", tags=["cutout", "local"], color="#334155")
A("real-esrgan", "Real-ESRGAN", "image-tools", "open-source", "free", "Upscale images and video frames", "Practical super-resolution for photos and frames.", {**gh("xinntao/Real-ESRGAN")}, "BSD-3", tags=["upscale", "local"], color="#7C2D12")
A("upscayl", "Upscayl", "image-tools", "open-source", "free", "Desktop image upscaler", "Free app to upscale images with AI models.", {"Website": "https://upscayl.org", **gh("upscayl/upscayl")}, "AGPL", integration=folder(), tags=["upscale", "desktop"], color="#4F46E5")
A("gfpgan", "GFPGAN", "image-tools", "open-source", "free", "Restore faces in photos", "Face restoration for old or low-quality photos.", {**gh("TencentARC/GFPGAN")}, "Apache-2.0", tags=["restore", "local"], color="#B91C1C")
A("sam2", "Segment Anything 2", "image-tools", "open-source", "free", "Segment and track any object", "Meta's model for masks in images and video.", {**gh("facebookresearch/sam2")}, "Apache-2.0", tags=["segmentation", "video"], color="#0866FF")
A("rife", "RIFE", "image-tools", "open-source", "free", "Smooth slow motion by frame interpolation", "Real-time intermediate flow estimation for video.", {**gh("hzwer/ECCV2022-RIFE")}, "MIT", tags=["interpolation", "video"], color="#059669")

# ---------------------------------------------------------------- design
A("canva", "Canva", "design", "service", "freemium", "Editable designs and brand kits", "Connect Canva in claude.ai to create, resize and export designs.", {"Website": "https://www.canva.com", "Connectors": "https://claude.ai/settings/connectors"}, tags=["design", "brand"], color="#00A3BF")
A("figma", "Figma", "design", "service", "freemium", "Design files Claude can read", "Figma's MCP server lets Claude read frames, styles and assets.", {"Website": "https://www.figma.com", "MCP docs": "https://developers.figma.com/docs/figma-mcp-server/"}, integration=mcp_http("figma", "https://mcp.figma.com/mcp", oauth=True), tags=["design", "mcp"], color="#A259FF")
A("penpot", "Penpot", "design", "open-source", "free", "Open-source design and prototyping", "Browser-based design tool built on open standards (SVG).", {"Website": "https://penpot.app", **gh("penpot/penpot")}, "MPL-2.0", tags=["design"], color="#000000")
A("excalidraw", "Excalidraw", "design", "open-source", "free", "Hand-drawn style diagrams", "Sketch diagrams for explainer videos and carousels.", {"Website": "https://excalidraw.com", **gh("excalidraw/excalidraw")}, "MIT", tags=["diagrams"], color="#6965DB")
A("photopea", "Photopea", "design", "service", "free", "Photoshop-like editor in the browser", "Edit PSD, XCF and Sketch files online.", {"Website": "https://www.photopea.com"}, integration=folder(), tags=["photo", "editing"], color="#18A497")
A("gimp", "GIMP", "design", "open-source", "free", "Free image editor", "Photo retouching and image composition.", {"Website": "https://www.gimp.org"}, "GPL", integration=folder(), tags=["photo", "desktop"], color="#5C5543")
A("inkscape", "Inkscape", "design", "open-source", "free", "Vector graphics editor", "Edit SVG logos and icons.", {"Website": "https://inkscape.org"}, "GPL", integration=folder(), tags=["vector", "desktop"], color="#000000")
A("krita", "Krita", "design", "open-source", "free", "Painting and illustration", "Digital painting for illustrated content.", {"Website": "https://krita.org"}, "GPL", integration=folder(), tags=["illustration", "desktop"], color="#3BABFF")

# ---------------------------------------------------------------- stock & fonts
A("pexels", "Pexels", "stock", "service", "free", "Free stock photos and videos", "High-quality free photos and b-roll with an API.", {"Website": "https://www.pexels.com", "API": "https://www.pexels.com/api/"}, integration=keys("PEXELS_API_KEY"), tags=["stock", "video", "photo"], color="#05A081")
A("unsplash", "Unsplash", "stock", "service", "free", "Free high-resolution photos", "Photo library with an API; follow its attribution guidelines.", {"Website": "https://unsplash.com", "API": "https://unsplash.com/developers"}, integration=keys("UNSPLASH_ACCESS_KEY"), tags=["stock", "photo"], color="#111111")
A("pixabay", "Pixabay", "stock", "service", "free", "Free images, video and music", "Royalty-free media with an API.", {"Website": "https://pixabay.com", "API": "https://pixabay.com/api/docs/"}, integration=keys("PIXABAY_API_KEY"), tags=["stock", "video", "music"], color="#2EC66D")
A("openverse", "Openverse", "stock", "service", "free", "Search openly licensed media", "Search CC-licensed images and audio across sources.", {"Website": "https://openverse.org"}, tags=["stock", "cc"], color="#FFE033")
A("coverr", "Coverr", "stock", "service", "free", "Free stock video for creators", "Free b-roll clips, many vertical.", {"Website": "https://coverr.co"}, integration=folder(), tags=["stock", "video"], color="#1C1C1C")
A("google-fonts", "Google Fonts", "stock", "service", "free", "Open fonts the studio already uses", "Every brand font in the studio loads from Google Fonts.", {"Website": "https://fonts.google.com"}, tags=["fonts"], color="#4285F4")
A("lucide", "Lucide", "stock", "open-source", "free", "Clean open-source icons", "The icon set used by the Studio UI.", {"Website": "https://lucide.dev", **gh("lucide-icons/lucide")}, "ISC", tags=["icons"], color="#F56565")
A("iconify", "Iconify", "stock", "open-source", "free", "200,000+ open icons in one place", "Unified access to many open icon sets.", {"Website": "https://iconify.design"}, tags=["icons"], color="#1769AA")

# ---------------------------------------------------------------- research & scraping
A("yt-dlp", "yt-dlp", "research", "open-source", "free", "Pull public posts from TikTok and YouTube", "The free scraper behind the Research page.", {**gh("yt-dlp/yt-dlp")}, "Unlicense", tags=["scraping", "cli"], color="#B91C1C")
A("apify", "Apify", "research", "service", "paid", "Instagram, Facebook and 5,000+ scrapers", "Paid-per-result scrapers; official MCP server.", {"Website": "https://apify.com", "MCP docs": "https://docs.apify.com/platform/integrations/mcp"}, integration=mcp_http("apify", "https://mcp.apify.com", "APIFY_TOKEN"), tags=["scraping", "social"], color="#2BA84A")
A("firecrawl", "Firecrawl", "research", "service", "freemium", "Turn websites into clean data", "Crawl and scrape sites into markdown for brand research. MCP server.", {"Website": "https://www.firecrawl.dev", **gh("firecrawl/firecrawl-mcp-server")}, integration=mcp_cmd("firecrawl", "npx", ["-y", "firecrawl-mcp"], "FIRECRAWL_API_KEY"), tags=["scraping", "web"], color="#FF6B00")
A("exa", "Exa", "research", "service", "freemium", "Search engine built for AI", "Find competitors, articles and trends. Hosted MCP server.", {"Website": "https://exa.ai", "MCP docs": "https://docs.exa.ai/reference/exa-mcp"}, integration=mcp_http("exa", "https://mcp.exa.ai/mcp"), tags=["search", "web"], color="#1E40AF")
A("tavily", "Tavily", "research", "service", "freemium", "Web search API for agents", "Real-time search and extraction. MCP server.", {"Website": "https://tavily.com", **gh("tavily-ai/tavily-mcp")}, integration=mcp_cmd("tavily", "npx", ["-y", "tavily-mcp"], "TAVILY_API_KEY"), tags=["search", "web"], color="#4F46E5")
A("bright-data", "Bright Data", "research", "service", "paid", "Web data at scale", "Proxies and ready datasets for social and e-commerce research.", {"Website": "https://brightdata.com"}, integration=keys("BRIGHTDATA_API_TOKEN"), tags=["scraping"], color="#3D7FFC")
A("playwright-mcp", "Playwright MCP", "research", "open-source", "free", "Let Claude drive a browser", "Microsoft's MCP server for browser automation.", {**gh("microsoft/playwright-mcp")}, "Apache-2.0", integration=mcp_cmd("playwright", "npx", ["-y", "@playwright/mcp@latest"]), tags=["browser", "mcp"], color="#2EAD33")

# ---------------------------------------------------------------- social APIs
A("meta-graph", "Meta Graph API", "social-apis", "service", "free", "Official Instagram and Facebook data", "Business Discovery for Instagram and your Facebook Pages.", {"Docs": "https://developers.facebook.com/docs/instagram-platform"}, integration=keys("META_ACCESS_TOKEN", "META_IG_USER_ID"), tags=["instagram", "facebook"], color="#0866FF")
A("youtube-data-api", "YouTube Data API", "social-apis", "service", "free", "Official YouTube channel and video data", "Search videos and read stats with a Google API key.", {"Docs": "https://developers.google.com/youtube/v3"}, integration=keys("YOUTUBE_API_KEY"), tags=["youtube"], color="#FF0000")
A("tiktok-api", "TikTok for Developers", "social-apis", "service", "free", "Official TikTok APIs", "Display, Content Posting and Research APIs (approval required).", {"Docs": "https://developers.tiktok.com"}, integration=keys("TIKTOK_CLIENT_KEY", "TIKTOK_CLIENT_SECRET"), tags=["tiktok"], color="#000000")
A("linkedin-api", "LinkedIn API", "social-apis", "service", "free", "Post and read LinkedIn content", "Share and Community Management APIs for pages.", {"Docs": "https://learn.microsoft.com/linkedin/"}, tags=["linkedin"], color="#0A66C2")
A("x-api", "X API", "social-apis", "service", "paid", "Post and search on X", "Official API for X (Twitter), tiered pricing.", {"Docs": "https://developer.x.com"}, integration=keys("X_BEARER_TOKEN"), tags=["x", "twitter"], color="#000000")
A("pinterest-api", "Pinterest API", "social-apis", "service", "free", "Create pins and read analytics", "Official API for pins, boards and analytics.", {"Docs": "https://developers.pinterest.com"}, tags=["pinterest"], color="#E60023")

# ---------------------------------------------------------------- publishing
A("postiz", "Postiz", "publishing", "open-source", "freemium", "Schedule posts to 20+ networks", "Open-source scheduler with an official MCP server; cloud or self-hosted.", {"Website": "https://postiz.com", **gh("gitroomhq/postiz-app"), "MCP docs": "https://docs.postiz.com/mcp/introduction"}, "AGPL-3.0", integration=mcp_http("postiz", "https://api.postiz.com/mcp", "POSTIZ_API_KEY"), tags=["scheduling", "mcp"], color="#612AD5")
A("mixpost", "Mixpost", "publishing", "open-source", "freemium", "Self-hosted social media management", "Schedule and analyze posts on your own server.", {"Website": "https://mixpost.app", **gh("inovector/mixpost")}, "MIT", tags=["scheduling", "self-hosted"], color="#4F46E5")
A("buffer", "Buffer", "publishing", "service", "freemium", "Simple social scheduling", "Plan and publish across major networks.", {"Website": "https://buffer.com"}, tags=["scheduling"], color="#231F20")
A("later", "Later", "publishing", "service", "paid", "Visual planner for Instagram and TikTok", "Drag-and-drop calendar with link in bio.", {"Website": "https://later.com"}, tags=["scheduling", "instagram"], color="#FA6B5D")
A("metricool", "Metricool", "publishing", "service", "freemium", "Plan, publish and analyze", "Scheduling with analytics and competitor tracking.", {"Website": "https://metricool.com"}, tags=["scheduling", "analytics"], color="#3E68F5")
A("hootsuite", "Hootsuite", "publishing", "service", "paid", "Social management for teams", "Publishing, inbox and reporting for many accounts.", {"Website": "https://www.hootsuite.com"}, tags=["scheduling", "teams"], color="#143059")
A("ayrshare", "Ayrshare", "publishing", "service", "paid", "Social posting API", "One API to post to many networks.", {"Website": "https://www.ayrshare.com"}, integration=keys("AYRSHARE_API_KEY"), tags=["scheduling", "api"], color="#E14D2A")
A("typefully", "Typefully", "publishing", "service", "freemium", "Write and schedule threads", "Drafting and scheduling for X, LinkedIn and Threads.", {"Website": "https://typefully.com"}, tags=["scheduling", "writing"], color="#1F1F1F")

# ---------------------------------------------------------------- analytics
A("plausible", "Plausible", "analytics", "open-source", "paid", "Privacy-friendly web analytics", "Simple analytics for link-in-bio and landing pages; self-hostable.", {"Website": "https://plausible.io", **gh("plausible/analytics")}, "AGPL", tags=["web", "privacy"], color="#5850EC")
A("umami", "Umami", "analytics", "open-source", "free", "Self-hosted website analytics", "Lightweight, privacy-focused analytics.", {"Website": "https://umami.is", **gh("umami-software/umami")}, "MIT", tags=["web", "self-hosted"], color="#000000")
A("posthog", "PostHog", "analytics", "open-source", "freemium", "Product analytics and more", "Events, funnels, session replay and experiments.", {"Website": "https://posthog.com", **gh("PostHog/posthog")}, "MIT", tags=["product", "web"], color="#F54E00")
A("dub", "Dub", "analytics", "open-source", "freemium", "Short links with click analytics", "Branded short links for captions and bios.", {"Website": "https://dub.co", **gh("dubinc/dub")}, "AGPL", integration=keys("DUB_API_KEY"), tags=["links"], color="#000000")

# ---------------------------------------------------------------- automation
A("n8n", "n8n", "automation", "open-source", "freemium", "Workflow automation you can self-host", "Connect apps and trigger the studio from schedules and webhooks.", {"Website": "https://n8n.io", **gh("n8n-io/n8n")}, "Sustainable Use License", tags=["automation", "self-hosted"], color="#EA4B71")
A("activepieces", "Activepieces", "automation", "open-source", "freemium", "Open automation with an MCP hub", "Automations and hundreds of integrations exposed to agents.", {"Website": "https://www.activepieces.com", **gh("activepieces/activepieces")}, "MIT", tags=["automation", "mcp"], color="#6E41E2")
A("zapier", "Zapier", "automation", "service", "freemium", "Connect 7,000+ apps", "Automations and a personal MCP endpoint for agents.", {"Website": "https://zapier.com", "MCP": "https://zapier.com/mcp"}, tags=["automation", "mcp"], color="#FF4F00")
A("make", "Make", "automation", "service", "freemium", "Visual automation scenarios", "Build multi-step automations visually.", {"Website": "https://www.make.com"}, tags=["automation"], color="#6D00CC")

# ---------------------------------------------------------------- storage & assets
A("notion", "Notion", "storage", "service", "freemium", "Briefs, calendars and docs", "Official hosted MCP server so Claude can read briefs and write calendars.", {"Website": "https://www.notion.so", "MCP docs": "https://developers.notion.com/docs/mcp"}, integration=mcp_http("notion", "https://mcp.notion.com/mcp", oauth=True), tags=["docs", "mcp"], color="#000000")
A("google-drive", "Google Drive", "storage", "service", "freemium", "Shared files and footage", "Sync a Drive folder locally and connect it as a Library folder.", {"Website": "https://drive.google.com"}, integration=folder(), tags=["storage"], color="#1FA463")
A("dropbox", "Dropbox", "storage", "service", "freemium", "File sync for teams", "Sync a Dropbox folder and connect it to the Library.", {"Website": "https://www.dropbox.com"}, integration=folder(), tags=["storage"], color="#0061FF")
A("cloudinary", "Cloudinary", "storage", "service", "freemium", "Media hosting and transformations", "Host, resize and transform images and video by URL.", {"Website": "https://cloudinary.com"}, integration=keys("CLOUDINARY_URL"), tags=["dam", "cdn"], color="#3448C5")
A("airtable", "Airtable", "storage", "service", "freemium", "Content calendars as databases", "Plan content in a database your team already uses.", {"Website": "https://www.airtable.com"}, integration=keys("AIRTABLE_API_KEY"), tags=["planning"], color="#FCB400")
A("supabase", "Supabase", "storage", "open-source", "freemium", "Postgres, storage and auth", "Store assets and content data; official hosted MCP server.", {"Website": "https://supabase.com", "MCP docs": "https://supabase.com/docs/guides/getting-started/mcp"}, "Apache-2.0", integration=mcp_http("supabase", "https://mcp.supabase.com/mcp", oauth=True), tags=["database", "mcp"], color="#3ECF8E")
A("github", "GitHub", "storage", "service", "freemium", "Version your studio and registries", "Official GitHub MCP server for repos, issues and PRs.", {"Website": "https://github.com", **gh("github/github-mcp-server")}, integration=mcp_http("github", "https://api.githubcopilot.com/mcp/", oauth=True), tags=["git", "mcp"], color="#181717")

# ---------------------------------------------------------------- Claude skills
A("anthropic-skills", "Anthropic skills", "skills", "skill", "free", "Decks, docs, PDFs and spreadsheets", "Anthropic's public skills: pptx, docx, pdf, xlsx and more.", {**gh("anthropics/skills")}, integration=skills("anthropics/skills"), tags=["skills", "documents"], color="#D97757")
A("remotion-skills", "Remotion skills", "skills", "skill", "free", "Best practices for Remotion", "Remotion's official agent skills for creating and rendering.", {**gh("remotion-dev/skills"), "Docs": "https://www.remotion.dev/docs/ai/skills"}, integration=skills("remotion-dev/skills"), tags=["skills", "video"], color="#0B84F3")
A("vercel-agent-skills", "Vercel agent skills", "skills", "skill", "free", "Web and React best practices", "Vercel's skills for React, Next.js and web design reviews.", {**gh("vercel-labs/agent-skills")}, integration=skills("vercel-labs/agent-skills"), tags=["skills", "web"], color="#000000")
A("supabase-skills", "Supabase skills", "skills", "skill", "free", "Supabase best practices for agents", "Guidance for building on Supabase safely.", {**gh("supabase/agent-skills")}, integration=skills("supabase/agent-skills"), tags=["skills", "database"], color="#3ECF8E")
A("superpowers", "Superpowers", "skills", "skill", "free", "A core skills library for Claude Code", "Planning, debugging and TDD workflows as skills.", {**gh("obra/superpowers")}, "MIT", integration=skills("obra/superpowers"), tags=["skills", "workflow"], color="#7C3AED")
A("skills-sh", "skills.sh", "skills", "service", "free", "Directory of agent skills", "Browse community skills, then add any repo here.", {"Website": "https://skills.sh"}, tags=["directory"], color="#111111")

# ---------------------------------------------------------------- MCP connectors (general)
A("context7", "Context7", "mcp", "service", "freemium", "Up-to-date library docs for Claude", "Fetches current documentation for libraries like Remotion and GSAP.", {"Website": "https://context7.com", **gh("upstash/context7")}, integration=mcp_http("context7", "https://mcp.context7.com/mcp"), tags=["docs", "mcp"], color="#059669")
A("mcp-registry", "MCP Registry", "mcp", "service", "free", "The official catalog of MCP servers", "Find more connectors to add with Add from a link.", {"Website": "https://registry.modelcontextprotocol.io"}, tags=["directory"], color="#000000")

# ---------------------------------------------------------------- local AI
A("pinokio", "Pinokio", "local-ai", "open-source", "free", "One-click local AI apps", "Install and run local AI tools; connect their output folders.", {"Website": "https://pinokio.co", **gh("pinokiocomputer/pinokio")}, "MIT", integration=folder(), tags=["launcher", "local"], color="#3F3F46")
A("ollama", "Ollama", "local-ai", "open-source", "free", "Run open LLMs locally", "Local language models for drafting captions offline.", {"Website": "https://ollama.com", **gh("ollama/ollama")}, "MIT", tags=["llm", "local"], color="#000000")
A("lm-studio", "LM Studio", "local-ai", "desktop", "free", "Desktop app for local LLMs", "Download and chat with open models on your computer.", {"Website": "https://lmstudio.ai"}, tags=["llm", "desktop"], color="#4338CA")
A("open-webui", "Open WebUI", "local-ai", "open-source", "free", "Self-hosted chat UI for local models", "A web interface for Ollama and OpenAI-compatible APIs.", {"Website": "https://openwebui.com", **gh("open-webui/open-webui")}, tags=["llm", "self-hosted"], color="#111827")
A("shopify", "Shopify", "storage", "service", "paid", "Product catalog for promos", "Pull products, prices and photos into product promos.", {"Website": "https://www.shopify.com", "Docs": "https://shopify.dev"}, integration=keys("SHOPIFY_STORE_DOMAIN", "SHOPIFY_ACCESS_TOKEN"), tags=["ecommerce", "products"], color="#95BF47")

CATEGORIES = [
    ["video-engines", "Video engines"], ["editors", "Video editors"], ["motion", "Motion & animation"],
    ["voice", "Voice & TTS"], ["voice-clone", "Voice cloning & conversion"], ["transcription", "Transcription"],
    ["music", "Music & sound"], ["audio-tools", "Audio cleanup"], ["image-gen", "Image generation"],
    ["video-gen", "Video generation"], ["avatars", "Avatars & lip-sync"], ["image-tools", "Upscaling & cutouts"],
    ["design", "Design"], ["stock", "Stock media & fonts"], ["research", "Research & scraping"],
    ["social-apis", "Social platform APIs"], ["publishing", "Publishing & scheduling"], ["analytics", "Analytics"],
    ["automation", "Automation"], ["storage", "Storage & workspace"], ["skills", "Claude skills"],
    ["mcp", "MCP connectors"], ["local-ai", "Local AI"],
]

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "apps"), exist_ok=True)
    seen = set()
    for a in APPS:
        assert a["id"] not in seen, a["id"]
        seen.add(a["id"])
        with open(os.path.join(ROOT, "apps", f"{a['id']}.json"), "w") as f:
            json.dump(a, f, indent=2, ensure_ascii=False)
            f.write("\n")
    with open(os.path.join(ROOT, "categories.json"), "w") as f:
        json.dump(CATEGORIES, f, indent=2)
        f.write("\n")
    print(f"wrote {len(APPS)} apps")
