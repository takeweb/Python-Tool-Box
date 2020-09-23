◆自力計算の方(元々2進数専用)
python decUtil.py -n 100 -d 2
1100100
python decUtil.py -n 100 -d 8
144
python decUtil.py -n 100 -d 16
64
python decUtil.py -n 26 -d 16
1A

python decUtil.py -m a2d -n 1100100 -d 2
100
python decUtil.py -m a2d -n 144 -d 8
100
python decUtil.py -m a2d -n 1A -d 16
26

◆新しい方(Pythonの関数を利用)
python conv_dec_to_n.py -n 100 -d 2
0b1100100
python conv_dec_to_n.py -n 100 -d 8
0o144
python conv_dec_to_n.py -n 100 -d 16
0x64

python conv_dec_to_n.py -m a2d -n 0b1100100 -d 2
100
python conv_dec_to_n.py -m a2d -n 0o144 -d 8
100
python conv_dec_to_n.py -m a2d -n 0x64 -d 16
100