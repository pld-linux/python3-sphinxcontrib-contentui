# TODO: doc (fails with package not installed already)
#
# Conditional build:
%bcond_with	doc	# API documentation

Summary:	Contentui extension for Sphinx
Summary(pl.UTF-8):	Rozszerzenie contentui dla Sphinksa
Name:		python3-sphinxcontrib-contentui
Version:	0.2.5
Release:	1
# tags and notes specify "BSD", but included LICENSE file is MIT???
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-contentui/
#Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-contentui/sphinxcontrib-contentui-%{version}.tar.gz
# since 0.2.3 only wheels published on pypi, so use git archive
Source0:	https://github.com/ulrobix/sphinxcontrib-contentui/archive/%{version}/sphinxcontrib-contentui-%{version}.tar.gz
# Source0-md5:	774a9e95c36665166aad0cf850c1dec1
URL:		https://pypi.org/project/sphinxcontrib-contentui/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3 >= 2.0
%endif
Requires:	python3-modules >= 1:3.2
Requires:	python3-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contentui is a modified fork of Serge Domkowski's "examplecode"
extension. This is a simple extension that is rendered as HTML
widgets for Sphinx:
- Content tab
- Column content
- Toggle header

%description -l pl.UTF-8
Contentui to zmodyfikowane odgałęzienie rozszerzenia "examplecode"
Serge'a Domkowskiego. Jest to proste rozszerzenie, renderowane jako
widżety HTML dla Sphinksa:
- zakładka treści
- kolumna treści
- nagłówek przełączania

%package apidocs
Summary:	API documentation for Python sphinxcontrib-contentui module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sphinxcontrib-contentui
Group:		Documentation

%description apidocs
API documentation for Python sphinxcontrib-contentui module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sphinxcontrib-contentui.

%prep
%setup -q -n sphinxcontrib-contentui-%{version}

%build
%py3_build

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/contentui.css
%{py3_sitescriptdir}/sphinxcontrib/contentui.js
%{py3_sitescriptdir}/sphinxcontrib/contentui.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/contentui.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_contentui-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_contentui-%{version}-py*-nspkg.pth
