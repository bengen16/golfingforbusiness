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


if __name__ == '__main__':
	postname = sys.argv[1]
	print(postname)
	f = createPost(postname)
	postname = postname.split('.')
	print(postname)
#	newf = open(f'{postname}.html', 'x')
#	newf.write(f)
	print(f)
