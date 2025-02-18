from utils import read_video, save_video
from trackers import Tracker

def main():
    video_frames = read_video('input_videos/teste1.webm')

    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')

    output_video_frames = tracker.draw_annotations(video_frames,tracks)

    save_video(video_frames, 'output_videos/output_video.mp4')

if __name__ == '__main__':
    main()