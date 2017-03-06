%global        uname wsgiref
%global        sum WSGI (PEP 333) Reference Library

Name:          python-%{uname}
Version:       0.1.2
Release:       1%{?dist}
Summary:       %{sum}

URL:           https://pypi.python.org/pypi/%{uname}
Source:        https://pypi.io/packages/source/w/%{uname}/%{uname}-%{version}.zip
License:       PSF or ZPL

BuildArch:     noarch

Buildrequires: python-setuptools
Buildrequires: python2-devel
Buildrequires: python-nose

%description
%{sum}.

%package -n python2-%{uname}
Summary:        %{sum}

%description -n python2-%{uname}
%{sum}.

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%check
%{__python2} setup.py test

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{uname}
%{python2_sitelib}/*

%changelog
* Mon Mar 6 2017 Nicolas Hicher <nhicher@redhat.com> 0.1.2-1
- initial package
