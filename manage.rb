#!/usr/bin/env ruby

INP = ARGV

if INP[0] == 'push'
	print "Commit: "
	com = STDIN.gets.chomp
	cmd1 = 'git add -A'
	cmd2 = "git commit -m " + "'" + com + "'" 
	cmd3 = 'git push'
	system(cmd1)
	system(cmd2)
	system(cmd3)
	puts "Done"
end

if INP[0] == 'start'
	cmd1 = 'cd backend && nohup ./manage.py runserver &'
	cmd2 = 'pm2 start GeekyChunk'
	system(cmd1)
	system(cmd2)
end

if INP[0] == 'run'
	puts 'Starting Development Server Do Not Close Window!'
	cmd1 = 'cd backend && ./manage.py runserver &'
	cmd2 = 'cd frontend && yarn dev &'
	system(cmd1)
	system(cmd2)
end