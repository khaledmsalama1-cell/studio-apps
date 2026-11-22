# studio-apps

The app registry for [Studio](https://github.com/khaledmsalama1-cell/studio): 167 tools, services, skills and MCP connectors for making brand content with Claude.

The Studio scans this repo (**Apps → Sources → Refresh**) and lists everything here on its Apps page, where each app can be connected in one click.

## How it works

- One file per app in [`apps/`](apps), validated by [`scripts/build-index.mjs`](scripts/build-index.mjs) into [`index.json`](index.json), which is what the Studio reads.
- Each app declares one **integration** the Studio applies *without running any code*:

| Integration | What the Studio does |
|---|---|
| `mcp` | Adds an MCP connector to the project's `.mcp.json` (remote URL, or an `npx`/`uvx` package), with keys kept in `.env` |
| `skills-repo` | Copies every folder with a `SKILL.md` from a GitHub repo into `.claude/skills` |
| `keys` | Asks for API keys and stores them in `.env` |
| `folder` | Connects the app's export folder to the Library, so its files can be used in projects |
| `link` | Information and links only |

Commands that install software are **never** accepted from this registry; only the Studio's own local catalogue can define them.

## Add an app

1. Create `apps/<id>.json` (copy any existing file; fields are described in [`schema.json`](schema.json)).
2. Run `node scripts/build-index.mjs`. It fails on anything invalid.
3. Commit `apps/<id>.json`, `index.json` and `README.md`.

Facts change fast: check links, licenses and pricing on the vendor's site before relying on them.

## Catalogue (167 apps)

15 with an MCP connector · 5 skill packs · 26 API-key integrations · 41 export-folder apps

### Video engines

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Blender](https://www.blender.org) | 3D, motion graphics and video editing | open-source (GPL) | free | folder |
| [FFmpeg](https://ffmpeg.org) | The video toolbox under everything | open-source (LGPL/GPL) | free | link |
| [HyperFrames](https://hyperframes.heygen.com) | Write HTML, render MP4 | open-source (Apache-2.0) | free | link |
| [Manim](https://www.manim.community) | Math and diagram animations in Python | open-source (MIT) | free | link |
| [Motion Canvas](https://motioncanvas.io) | Animations written in TypeScript | open-source (MIT) | free | link |
| [Remotion](https://www.remotion.dev) | Videos as React components | open-source (Remotion License) | freemium | link |
| [Revideo](https://re.video) | Motion Canvas, built for rendering at scale | open-source (MIT) | free | link |

### Video editors

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [auto-editor](https://github.com/WyattBlue/auto-editor) | Cut silences automatically | open-source (Unlicense) | free | link |
| [CapCut](https://www.capcut.com) | Mobile-first editor with templates | service | freemium | folder |
| [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | Pro editing, color and audio | desktop | freemium | folder |
| [Descript](https://www.descript.com) | Edit video by editing the transcript | service | freemium | folder |
| [Kdenlive](https://kdenlive.org) | Full non-linear video editor | open-source (GPL) | free | folder |
| [OBS Studio](https://obsproject.com) | Record and stream your screen and camera | open-source (GPL) | free | folder |
| [OpenShot](https://www.openshot.org) | Simple video editor | open-source (GPL) | free | folder |
| [Opus Clip](https://www.opus.pro) | Long video into viral shorts | service | freemium | folder |
| [Shotcut](https://shotcut.org) | Cross-platform video editor | open-source (GPL) | free | folder |
| [Submagic](https://www.submagic.co) | Animated captions for shorts | service | paid | folder |

### Motion & animation

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [GSAP](https://gsap.com) | The animation library HyperFrames uses | open-source | free | link |
| [Lottie](https://airbnb.io/lottie) | Lightweight vector animations | open-source (MIT) | free | link |
| [LottieFiles](https://lottiefiles.com) | Library of ready Lottie animations | service | freemium | link |
| [Rive](https://rive.app) | Interactive animations with state machines | service | freemium | link |
| [Theatre.js](https://www.theatrejs.com) | Motion design editor for the web | open-source (Apache-2.0) | free | link |
| [Three.js](https://threejs.org) | 3D in the browser | open-source (MIT) | free | link |

### Voice & TTS

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Bark](https://github.com/suno-ai/bark) | Text to audio with laughs and music | open-source (MIT) | free | link |
| [Cartesia](https://cartesia.ai) | Ultra-low-latency voice API | service | paid | keys |
| [Chatterbox](https://github.com/resemble-ai/chatterbox) | Expressive open TTS with cloning | open-source (MIT) | free | link |
| [Coqui TTS](https://github.com/coqui-ai/TTS) | Toolkit with XTTS and many models | open-source (MPL-2.0) | free | link |
| [Dia](https://github.com/nari-labs/dia) | Realistic two-speaker dialogue | open-source (Apache-2.0) | free | link |
| [ElevenLabs](https://elevenlabs.io) | The voices people can't tell from real | service | freemium | mcp |
| [F5-TTS](https://github.com/SWivid/F5-TTS) | Zero-shot voice cloning TTS | open-source (MIT (code)) | free | link |
| [Fish Speech / OpenAudio](https://fish.audio) | Multilingual TTS and cloning | open-source | freemium | link |
| [Kokoro](https://github.com/hexgrad/kokoro) | Small, fast, free local TTS | open-source (Apache-2.0) | free | link |
| [OpenAI TTS](https://platform.openai.com/docs/guides/text-to-speech) | Speech from the OpenAI API | service | paid | keys |
| [Orpheus TTS](https://github.com/canopyai/Orpheus-TTS) | Human-sounding open TTS | open-source (Apache-2.0) | free | link |
| [Piper](https://github.com/OHF-Voice/piper1-gpl) | Fast offline TTS for many languages | open-source (GPL-3.0) | free | link |
| [Sesame CSM](https://github.com/SesameAILabs/csm) | Conversational speech model | open-source (Apache-2.0) | free | link |
| [StyleTTS 2](https://github.com/yl4579/StyleTTS2) | Human-level TTS research model | open-source (MIT) | free | link |
| [Voicebox](https://github.com/jamiepine/voicebox) | An open-source voice studio | open-source (MIT) | free | folder |

### Voice cloning & conversion

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Applio](https://applio.org) | Friendly voice conversion app | open-source (MIT) | free | folder |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | Instant voice cloning | open-source (MIT) | free | link |
| [RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | Retrieval-based voice conversion | open-source (MIT) | free | link |

### Transcription

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [AssemblyAI](https://www.assemblyai.com) | Speech AI models via API | service | freemium | keys |
| [Deepgram](https://deepgram.com) | Speech-to-text API | service | freemium | keys |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Up to 4x faster Whisper | open-source (MIT) | free | link |
| [NVIDIA Parakeet](https://github.com/NVIDIA/NeMo) | Fast, accurate English ASR | open-source (Apache-2.0) | free | link |
| [Whisper](https://github.com/openai/whisper) | Speech recognition in 99 languages | open-source (MIT) | free | link |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Whisper in fast C/C++ | open-source (MIT) | free | link |
| [WhisperX](https://github.com/m-bain/whisperX) | Word-level timestamps and speakers | open-source (BSD-2) | free | link |

### Music & sound

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [ACE-Step](https://github.com/ace-step/ACE-Step) | Open music foundation model | open-source (Apache-2.0) | free | link |
| [Artlist](https://artlist.io) | Music, SFX and footage license | service | paid | folder |
| [AudioCraft (MusicGen)](https://github.com/facebookresearch/audiocraft) | Meta's open music and audio models | open-source (MIT (code)) | free | link |
| [Epidemic Sound](https://www.epidemicsound.com) | Licensed music for social | service | paid | folder |
| [Freesound](https://freesound.org) | Creative Commons sound effects | service | free | keys |
| [Stable Audio Open](https://github.com/Stability-AI/stable-audio-tools) | Open text-to-audio model | open-source | free | link |
| [Suno](https://suno.com) | Songs from a prompt | service | freemium | folder |
| [Udio](https://www.udio.com) | AI music generation | service | freemium | folder |
| [YouTube Audio Library](https://studio.youtube.com) | Free music for YouTube | service | free | folder |
| [YuE](https://github.com/multimodal-art-projection/YuE) | Open full-song generation | open-source (Apache-2.0) | free | link |

### Audio cleanup

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Adobe Podcast Enhance](https://podcast.adobe.com/enhance) | Make any recording sound studio-made | service | freemium | folder |
| [Audacity](https://www.audacityteam.org) | Record and edit audio | open-source (GPL) | free | folder |
| [Demucs](https://github.com/adefossez/demucs) | Separate vocals, drums and bass | open-source (MIT) | free | link |
| [Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui) | Vocal removal desktop app | open-source (MIT) | free | folder |

### Image generation

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [ComfyUI](https://www.comfy.org) | Node-based image and video generation | open-source (GPL) | free | folder |
| [FLUX](https://bfl.ai) | State-of-the-art image models | open-source | freemium | link |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Prompt-first image generation | open-source (GPL) | free | folder |
| [Gemini image (Imagen)](https://ai.google.dev/gemini-api/docs/image-generation) | Google's image generation and editing | service | paid | keys |
| [Ideogram](https://ideogram.ai) | Images with readable text | service | freemium | folder |
| [InvokeAI](https://invoke.com) | Creative studio for diffusion models | open-source (Apache-2.0) | free | folder |
| [Krea](https://www.krea.ai) | Real-time generation and enhancing | service | freemium | folder |
| [Leonardo.Ai](https://leonardo.ai) | Image and video generation suite | service | freemium | keys |
| [Midjourney](https://www.midjourney.com) | Distinctive image generation | service | paid | folder |
| [OpenAI Images](https://platform.openai.com/docs/guides/image-generation) | Image generation from the OpenAI API | service | paid | keys |
| [Recraft](https://www.recraft.ai) | Brand-consistent images and vectors | service | freemium | keys |
| [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | The classic Stable Diffusion UI | open-source (AGPL) | free | folder |

### Video generation

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [CogVideoX](https://github.com/THUDM/CogVideo) | Open text-to-video model | open-source (Apache-2.0) | free | link |
| [fal](https://fal.ai) | 1,000+ image, video and audio models | service | paid | mcp |
| [Google Veo](https://ai.google.dev/gemini-api/docs/video) | Google's video model with audio | service | paid | keys |
| [Higgsfield](https://higgsfield.ai) | Camera-motion presets for AI video | service | paid | folder |
| [HunyuanVideo](https://github.com/Tencent/HunyuanVideo) | Tencent's open video model | open-source | free | link |
| [Kling](https://klingai.com) | High-motion video generation | service | freemium | folder |
| [LTX-Video](https://github.com/Lightricks/LTX-Video) | Fast open video generation | open-source | free | link |
| [Luma Dream Machine](https://lumalabs.ai) | Cinematic video from text and images | service | freemium | keys |
| [MiniMax Hailuo](https://hailuoai.video) | Video generation with strong motion | service | freemium | folder |
| [Mochi](https://github.com/genmoai/mochi) | Open video model from Genmo | open-source (Apache-2.0) | free | link |
| [Pika](https://pika.art) | Playful video effects and generation | service | freemium | folder |
| [Replicate](https://replicate.com) | Run open models in the cloud | service | paid | mcp |
| [Runway](https://runwayml.com) | Gen video models and editing tools | service | paid | keys |
| [Wan](https://github.com/Wan-Video/Wan2.1) | Open video generation models | open-source (Apache-2.0) | free | link |

### Avatars & lip-sync

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [D-ID](https://www.d-id.com) | Talking photos and agents | service | paid | keys |
| [HeyGen](https://www.heygen.com) | AI avatars that present for you | service | paid | mcp |
| [LatentSync](https://github.com/bytedance/LatentSync) | High-quality open lip-sync | open-source (Apache-2.0) | free | link |
| [LivePortrait](https://github.com/KwaiVGI/LivePortrait) | Animate a portrait from a driving video | open-source (MIT) | free | link |
| [SadTalker](https://github.com/OpenTalker/SadTalker) | Talking head from one image and audio | open-source (Apache-2.0) | free | link |
| [Synthesia](https://www.synthesia.io) | Avatar videos for business | service | paid | folder |
| [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) | Lip-sync any video to audio | open-source | free | link |

### Upscaling & cutouts

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [BiRefNet](https://github.com/ZhengPeng7/BiRefNet) | Precise background removal | open-source (MIT) | free | link |
| [GFPGAN](https://github.com/TencentARC/GFPGAN) | Restore faces in photos | open-source (Apache-2.0) | free | link |
| [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | Upscale images and video frames | open-source (BSD-3) | free | link |
| [rembg](https://github.com/danielgatis/rembg) | Remove image backgrounds | open-source (MIT) | free | link |
| [RIFE](https://github.com/hzwer/ECCV2022-RIFE) | Smooth slow motion by frame interpolation | open-source (MIT) | free | link |
| [Segment Anything 2](https://github.com/facebookresearch/sam2) | Segment and track any object | open-source (Apache-2.0) | free | link |
| [Upscayl](https://upscayl.org) | Desktop image upscaler | open-source (AGPL) | free | folder |

### Design

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Canva](https://www.canva.com) | Editable designs and brand kits | service | freemium | link |
| [Excalidraw](https://excalidraw.com) | Hand-drawn style diagrams | open-source (MIT) | free | link |
| [Figma](https://www.figma.com) | Design files Claude can read | service | freemium | mcp |
| [GIMP](https://www.gimp.org) | Free image editor | open-source (GPL) | free | folder |
| [Inkscape](https://inkscape.org) | Vector graphics editor | open-source (GPL) | free | folder |
| [Krita](https://krita.org) | Painting and illustration | open-source (GPL) | free | folder |
| [Penpot](https://penpot.app) | Open-source design and prototyping | open-source (MPL-2.0) | free | link |
| [Photopea](https://www.photopea.com) | Photoshop-like editor in the browser | service | free | folder |

### Stock media & fonts

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Coverr](https://coverr.co) | Free stock video for creators | service | free | folder |
| [Google Fonts](https://fonts.google.com) | Open fonts the studio already uses | service | free | link |
| [Iconify](https://iconify.design) | 200,000+ open icons in one place | open-source | free | link |
| [Lucide](https://lucide.dev) | Clean open-source icons | open-source (ISC) | free | link |
| [Openverse](https://openverse.org) | Search openly licensed media | service | free | link |
| [Pexels](https://www.pexels.com) | Free stock photos and videos | service | free | keys |
| [Pixabay](https://pixabay.com) | Free images, video and music | service | free | keys |
| [Unsplash](https://unsplash.com) | Free high-resolution photos | service | free | keys |

### Research & scraping

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Apify](https://apify.com) | Instagram, Facebook and 5,000+ scrapers | service | paid | mcp |
| [Bright Data](https://brightdata.com) | Web data at scale | service | paid | keys |
| [Exa](https://exa.ai) | Search engine built for AI | service | freemium | mcp |
| [Firecrawl](https://www.firecrawl.dev) | Turn websites into clean data | service | freemium | mcp |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Let Claude drive a browser | open-source (Apache-2.0) | free | mcp |
| [Tavily](https://tavily.com) | Web search API for agents | service | freemium | mcp |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Pull public posts from TikTok and YouTube | open-source (Unlicense) | free | link |

### Social platform APIs

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [LinkedIn API](https://learn.microsoft.com/linkedin/) | Post and read LinkedIn content | service | free | link |
| [Meta Graph API](https://developers.facebook.com/docs/instagram-platform) | Official Instagram and Facebook data | service | free | keys |
| [Pinterest API](https://developers.pinterest.com) | Create pins and read analytics | service | free | link |
| [TikTok for Developers](https://developers.tiktok.com) | Official TikTok APIs | service | free | keys |
| [X API](https://developer.x.com) | Post and search on X | service | paid | keys |
| [YouTube Data API](https://developers.google.com/youtube/v3) | Official YouTube channel and video data | service | free | keys |

### Publishing & scheduling

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Ayrshare](https://www.ayrshare.com) | Social posting API | service | paid | keys |
| [Buffer](https://buffer.com) | Simple social scheduling | service | freemium | link |
| [Hootsuite](https://www.hootsuite.com) | Social management for teams | service | paid | link |
| [Later](https://later.com) | Visual planner for Instagram and TikTok | service | paid | link |
| [Metricool](https://metricool.com) | Plan, publish and analyze | service | freemium | link |
| [Mixpost](https://mixpost.app) | Self-hosted social media management | open-source (MIT) | freemium | link |
| [Postiz](https://postiz.com) | Schedule posts to 20+ networks | open-source (AGPL-3.0) | freemium | mcp |
| [Typefully](https://typefully.com) | Write and schedule threads | service | freemium | link |

### Analytics

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Dub](https://dub.co) | Short links with click analytics | open-source (AGPL) | freemium | keys |
| [Plausible](https://plausible.io) | Privacy-friendly web analytics | open-source (AGPL) | paid | link |
| [PostHog](https://posthog.com) | Product analytics and more | open-source (MIT) | freemium | link |
| [Umami](https://umami.is) | Self-hosted website analytics | open-source (MIT) | free | link |

### Automation

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Activepieces](https://www.activepieces.com) | Open automation with an MCP hub | open-source (MIT) | freemium | link |
| [Make](https://www.make.com) | Visual automation scenarios | service | freemium | link |
| [n8n](https://n8n.io) | Workflow automation you can self-host | open-source (Sustainable Use License) | freemium | link |
| [Zapier](https://zapier.com) | Connect 7,000+ apps | service | freemium | link |

### Storage & workspace

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Airtable](https://www.airtable.com) | Content calendars as databases | service | freemium | keys |
| [Cloudinary](https://cloudinary.com) | Media hosting and transformations | service | freemium | keys |
| [Dropbox](https://www.dropbox.com) | File sync for teams | service | freemium | folder |
| [GitHub](https://github.com) | Version your studio and registries | service | freemium | mcp |
| [Google Drive](https://drive.google.com) | Shared files and footage | service | freemium | folder |
| [Notion](https://www.notion.so) | Briefs, calendars and docs | service | freemium | mcp |
| [Shopify](https://www.shopify.com) | Product catalog for promos | service | paid | keys |
| [Supabase](https://supabase.com) | Postgres, storage and auth | open-source (Apache-2.0) | freemium | mcp |

### Claude skills

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Anthropic skills](https://github.com/anthropics/skills) | Decks, docs, PDFs and spreadsheets | skill | free | skills-repo |
| [Remotion skills](https://github.com/remotion-dev/skills) | Best practices for Remotion | skill | free | skills-repo |
| [skills.sh](https://skills.sh) | Directory of agent skills | service | free | link |
| [Supabase skills](https://github.com/supabase/agent-skills) | Supabase best practices for agents | skill | free | skills-repo |
| [Superpowers](https://github.com/obra/superpowers) | A core skills library for Claude Code | skill (MIT) | free | skills-repo |
| [Vercel agent skills](https://github.com/vercel-labs/agent-skills) | Web and React best practices | skill | free | skills-repo |

### MCP connectors

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [Context7](https://context7.com) | Up-to-date library docs for Claude | service | freemium | mcp |
| [MCP Registry](https://registry.modelcontextprotocol.io) | The official catalog of MCP servers | service | free | link |

### Local AI

| App | What it does | Type | Price | Studio integration |
|---|---|---|---|---|
| [LM Studio](https://lmstudio.ai) | Desktop app for local LLMs | desktop | free | link |
| [Ollama](https://ollama.com) | Run open LLMs locally | open-source (MIT) | free | link |
| [Open WebUI](https://openwebui.com) | Self-hosted chat UI for local models | open-source | free | link |
| [Pinokio](https://pinokio.co) | One-click local AI apps | open-source (MIT) | free | folder |
