# filtering 함수
# 버터워스 필터링 수행
# LPF : low_pass_filter
# HPF : high_pass_filter
# BPF : band_pass_filter


import numpy
from scipy.signal import butter, filtfilt


# Low Pass Filter
# param data : 입력 데이터
# param cutoff : 차단 주파수
# param fs : sampling 주파수
# param order : 차수
# return : 필터링 데이터
def low_pass_filter(data, cutoff, fs, order=2):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y


# High Pass Filter
# param data : 입력 데이터
# param cutoff : 차단 주파수
# param fs : sampling 주파수
# param order : 차수
# return : 필터링 데이터
def high_pass_filter(data, cutoff, fs, order=2):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    y = filtfilt(b, a, data)
    return y


# Band Pass Filter
# param data : 입력 데이터
# param low_cutoff, high_cutoff : 차단 주파수
# param fs : sampling 주파수
# param order : 차수
# return : 필터링 데이터
def band_pass_filter(data, low_cutoff, high_cutoff, fs, order=2):
    nyquist = 0.5 * fs
    low = low_cutoff / nyquist
    high = high_cutoff / nyquist
    b, a = butter(order, [low, high], btype='band', analog=False)
    y = filtfilt(b, a, data)


# Notch Pass Filter
# param data : 입력 데이터
# param cutoff : 차단 주파수
# param fs : sampling 주파수
# param quality : 품질계수
# return : 필터링 데이터
def notch_filter(data, cutoff, fs, quality=30):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(2, [normal_cutoff - 1/quality, normal_cutoff + 1/quality], btype='bandstop', analog=False)
    y = filtfilt(b, a, data)
    return y