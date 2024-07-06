all = ''
all_en = ''

def read_md(path)
  File.read(path).gsub(/^#/, '##')
end

%w(amylase kawatea kenkoooo mkut osak yuusti).each do |name|
  all += <<END
# #{name}
#{read_md("#{name}.md")}
END
  
  all_en += <<END
# #{name}
#{read_md("#{name}.en.md")}
END
end

File.open('all.md', 'w') {|f| f.puts(all) }
File.open('all.en.md', 'w') {|f| f.puts(all_en) }
