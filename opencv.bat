ONopencv_createsamples.exe -info info.txt -num 831 """change the number with the count of your negativ images""" -vec pos.vec
ONopencv_traincascade.exe -data data -vec pos.vec -bg bg.txt -numStages 10
