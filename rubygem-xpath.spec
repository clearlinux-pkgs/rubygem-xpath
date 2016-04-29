#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-xpath
Version  : 2.0.0
Release  : 7
URL      : https://rubygems.org/downloads/xpath-2.0.0.gem
Source0  : https://rubygems.org/downloads/xpath-2.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-disposable
BuildRequires : rubygem-mini_portile
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-yard

%description
# XPath
XPath is a Ruby DSL around a subset of XPath 1.0. Its primary purpose is to
facilitate writing complex XPath queries from Ruby code.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n xpath-2.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-xpath.gemspec

%build
gem build rubygem-xpath.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
xpath-2.0.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/xpath-2.0.0
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/xpath-2.0.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/lib/xpath.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/lib/xpath/dsl.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/lib/xpath/expression.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/lib/xpath/html.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/lib/xpath/literal.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/lib/xpath/renderer.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/lib/xpath/union.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/lib/xpath/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/spec/fixtures/form.html
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/spec/fixtures/simple.html
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/spec/fixtures/stuff.html
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/spec/html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/spec/union_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/xpath-2.0.0/spec/xpath_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/xpath-2.0.0.gemspec
