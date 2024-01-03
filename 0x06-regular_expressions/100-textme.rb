#!/usr/bin/env ruby
#Matching a string that starts with h and end with n
#and can have any string character in between
re = /[\w\s\:\-\[\]+,\S]+from:([\w+]+)\][\w\s\:\-\[\]+,\S]+to:([\w+]+)\][\w\s\:\-\[\]+,\S]+flags:([\w+-\:]+)\][\w\s\:\-\[\]+,\S]+/
reg = /.*from:([\w\+]+)\].*to:([\w\+]+)\].*flags:([\w\+\-\:]+).*/
matches = ARGV[0].scan(re)
if matches.any?
  timestamp, sender, message = matches[0]
  puts "#{timestamp},#{sender},#{message}"
end
