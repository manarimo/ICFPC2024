#!/usr/bin/env ruby
require 'pp'

ORDER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n"

def enc_string(str)
  str.chars.map {|c|
    (33 + ORDER.index(c)).chr
  }.join
end

def enc_number(num)
  if num == 0
    return "!"
  end
  buf = []
  while num > 0
    ord = num % 94
    buf << (33 + ord).chr
    num /= 94
  end
  buf.reverse.join
end

def tokenize(code)
  lines = code.split("\n")
  lines.map { |line|
    buf = []
    acc = ""
    context = nil

    line.split(/([ \t])/)
      .map { |t| 
        if t[0] != 'S' && t[0] != 'I' && t[0] != '!'
          t.split(/[()]/)
        else
          [t]
        end
      }
        .flatten
      .filter { |s| s != '' } + ["\n"]
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
    when /^S/
      if token[1] == ')' || token[-1] == ')'
        STDERR.puts "Syntax error: Use `!S` to allow `)` on the start or end of a string"
        exit 1
      end
      tokens_to_emit << token
    when /^I/
      if token[1] == ')' || token[-1] == ')'
        STDERR.puts "Syntax error: Use `!I` to allow `)` on the start or end of a number"
        exit 1
      end
      tokens_to_emit << token
    when /^!S/
      # Unchecked literal string
      tokens_to_emit << token[1..]
    when /^!I/
      # Unchecked literal number
      tokens_to_emit << token[1..]
    when /^@S/
      # Human-readble string macro
      # Escape sequences: @@ -> @, @_ -> _
      human_str = token[2..].gsub(/@([@_])/) { |m|
        case m[1]
        when '@'
          '@'
        when '_'
          ' '
        end
      }
      tokens_to_emit << "S#{enc_string(human_str)}"
    when /^@I/
      # Human-readable number
      human_num = token[2..].to_i
      tokens_to_emit << "I#{enc_number(human_num)}"
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
if !$TEST
  code = File.read(ARGV[0])
  tokens = tokenize(code)
  cst = parse(tokens)
  puts print_nodes(cst)
end
