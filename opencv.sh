opencv_createsamples -info info.txt -num 831 """change the number with the count of your negativ images""" -vec pos.vec
opencv_traincascade -data data -vec pos.vec -bg bg.txt
