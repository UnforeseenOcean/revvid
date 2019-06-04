import os
from moviepy.editor import *


def composite_video():

    moviesize = (1280, 720)

    directory = sorted(os.listdir("dump"))

    audio_clips = [
        AudioFileClip(f"dump/{x}") for x in directory if x.startswith("audio")
    ]

    image_clips = [ImageClip(f"dump/{x}") for x in directory if x.startswith("comment")]

    background = ColorClip(moviesize, color=(26, 26, 27))

    intermission = (
        VideoFileClip("data/transition.mp4").set_duration(1).resize(height=720)
    )

    title = CompositeVideoClip(
        [background, ImageClip("dump/post.png").set_pos("center").resize(0.8)],
        size=moviesize,
    ).set_audio(AudioFileClip("title.mp3"))

    final = [title]

    for audio, image in zip(audio_clips, image_clips):
        clip = (
            CompositeVideoClip(
                [background, image.set_pos("center").resize(0.8)], size=moviesize
            )
            .set_duration(audio.duration)
            .set_audio(audio)
        )
        final.append(clip)
        final.append(intermission)

    concatenate_videoclips(final).write_videofile(
        "dump/video.mp4", fps=20, codec="libx264", audio_codec="aac"
    )


composite_video()
