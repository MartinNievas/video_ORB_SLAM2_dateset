import numpy as np
import cv2
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split video frames into pictures for run ORBSLAM2 test')
    parser.add_argument('--video', type=str, required=True,
                        help='Input video file')
    parser.add_argument('--frames', type=str, required=True,
                        help='Output folder')

    args = parser.parse_args()

    cap = cv2.VideoCapture(args.video)
    f = open('time_stamp.txt', 'w')
    
    cont = 0
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret:
            print(cont)
            cv2.imshow('frame',frame)
            cv2.imwrite(args.frames+str(cont)+'.png',frame)
            f.write(str(cont)+str("\n"))
            cont += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    f.close()
    cap.release()
    cv2.destroyAllWindows()
    
