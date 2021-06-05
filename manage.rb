#!/usr/bin/env ruby

INP = ARGV

if (INP[0] == 'push')
	print "Commit: "
	com = STDIN.gets.chomp
	cmd1 = 'git add -A'
	cmd2 = "git commit -m " + "'" + com + "'" 
	cmd3 = 'git push'
	system(cmd1)
	system(cmd2)
	system(cmd3)	
end