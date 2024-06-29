#!/usr/bin/env ruby
require 'pp'

def tokenize(code)
  lines = code.split("\n")
  lines.map { |line|
    line.split(/([() \t])/).filter { |s| s != '' } + ["\n"]
  }.flatten
end

def parse(tokens)
  buf = []
  in_comment = false
  tokens.each do |token|
    tokens_to_emit = []

    case token
    when '--'
      # Comment until end of the line
      in_comment = true
    when "\n"
      in_comment = false
    when '('
    when ')'
    when /^\s+$/
      # Ignore for now
    else
      tokens_to_emit << token
    end

    if !in_comment
      buf.push(*tokens_to_emit)
    end
  end

  buf
end

def print_nodes(nodes)
  buf = []
  nodes.each do |node|
    buf << node
  end

  buf.join(' ')
end

######### main #########
code = File.read(ARGV[0])
tokens = tokenize(code)
cst = parse(tokens)
puts print_nodes(cst)
