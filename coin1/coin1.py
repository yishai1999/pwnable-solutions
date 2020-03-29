# flag: b1NaRy_S34rch1nG_1s_3asy_p3asy
import socket

#HOSTNAME = '0'
HOSTNAME = 'pwnable.kr'

q_count = 0

def answer_question(soc):
	global q_count
	q_count += 1
	question = soc.recv(2048).decode()
	print('Question #{}: {}'.format(q_count, question))
	n = int(question.split(' ')[0][2:])
	c = int(question.split(' ')[1][2:])
	left = 0
	right = n
	count = 1
	while True:
		query = ' '.join([str(i) for i in range(left, (left + right) //2)])
		query += '\n'
		soc.send(query.encode())
		print('{}/{}: {}-{}'.format(count,c,left,right))
		count += 1
		answer = soc.recv(1024).decode()
		print('[Server] ' + answer)
		if 'orrect' in answer:
			break
		elif int(answer) == 9:
			continue
		elif int(answer) == 10:
			left += 1
			right += 1
			continue
		elif int(answer) % 10 == 0:
			left = (left + right) // 2
		else:
			right = (left + right) // 2

def main():
	soc = socket.socket()
	soc.connect((HOSTNAME, 9007))

	message = ''
	while 'starting in' not in message:
		message = soc.recv(2048).decode()

	for i in range(100):
		answer_question(soc)
	message = soc.recv(2048).decode()
	print('last message: {}'.format(message))

main()
