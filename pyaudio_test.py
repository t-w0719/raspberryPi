# -*- coding: utf-8 -*-
#マイク0番からの入力を受ける。一定時間(RECROD_SECONDS)だけ録音し、ファイル名：mono.wavで保存する。
 
import pyaudio
import sys
import time
import wave
 
if __name__ == '__main__':
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    #サンプリングレート、マイク性能に依存
    RATE = 16000
    #録音時間
    RECORD_SECONDS = input('Please input recoding time>>>')
     
    #pyaudio
    p = pyaudio.PyAudio()
 
    #マイク0番を設定
    input_device_index = 0
    #マイクからデータ取得
    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)
    all = []
    for i in range(0, RATE / chunk * RECORD_SECONDS):
        data = stream.read(chunk)
        all.append(data)
 
    stream.close()    
    data = ''.join(all)                    
    out = wave.open('mono.wav','w')
    out.setnchannels(1) #mono
    out.setsampwidth(2) #16bits
    out.setframerate(RATE)
    out.writeframes(data)
    out.close()
     
    p.terminate()
