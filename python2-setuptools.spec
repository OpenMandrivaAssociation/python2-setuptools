%define module setuptools
%define _xz_threads 0

Summary:	Python 2.0 Distutils Enhancements
Name:		python2-%{module}
Version:	46.4.0
Release:	2
License:	Zope Public License (ZPL)
Group:		Development/Python
Url:		https://pypi.org/project/setuptools/
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools/setuptools-%{version}.zip
BuildArch:	noarch
BuildRequires:	python2
#BuildRequires:	python2-packaging
#BuildRequires:	python2-appdirs
Requires:	python2-pkg-resources

%description
A collection of enhancements to the Python 2.x distutils that allow
you to more easily build and distribute Python packages, especially
ones that have dependencies on other packages.

%package -n python2-pkg-resources
Summary:	Runtime module to access python 2 resources
Group:		Development/Python
#Requires:	python2-packaging
#Requires:	python2-appdirs

%description -n python2-pkg-resources
Module used to find and manage Python 2.x package/version dependencies and access
bundled files and resources, including those inside of zipped .egg files.

%prep
%autosetup -n %{module}-%{version}

%build
export CFLAGS="%{optflags}"

python2 setup.py build

%check
#%__python setup.py test

%install
python2 setup.py install --root=%{buildroot}
find %{buildroot}%{python2_sitelib} -name '*.exe' -delete
# Don't conflict with the python3 version
rm -f %{buildroot}%{_bindir}/easy_install

%files
%{_bindir}/easy_install-%{py2_ver}
%{py2_puresitedir}/*
%exclude %{py2_puresitedir}/pkg_resources

%files -n python2-pkg-resources
%{py2_puresitedir}/pkg_resources
