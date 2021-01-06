import os, sys
import markdown

def createPost(postName):
	assert os.walk(postName) != None
	postBod = open(f'{postName}', 'r')
	body = postBod.read()
	postBod.close()
	body = markdown.markdown(body)

	tempfd = open('template.html', 'r')
	template = tempfd.read()
	tempfd.close()

	halves = template.split('HERE')
	final = halves[0] + body + halves[1]
	return final

def updateLinks(postname):
	# painfully inefficient. Where's SED -i @?
	archfd = open('../archive.html', 'r')
	arch = archfd.read()
	archfd.close()
	# bad engineering woooooo
	arch = arch.split('<!-- BAD -->')
	newlink = f'<!-- BAD -->\n<a href="posts/{postname}.html"><h3>{postname}</h3></a>'
	arch = arch[0] + newlink + arch[1]
	archfd = open('../archive.html', 'w')
	archfd.write(arch)
	archfd.close()


if __name__ == '__main__':
	postname = sys.argv[1]
	f = createPost(postname)

	os.remove(f'{postname}')

	postname = postname.split('.')[0]
	newf = open(f'{postname}.html', 'x')
	newf.write(f)
	updateLinks(postname)
	print(f'"Successfully" added new post {postname}')
