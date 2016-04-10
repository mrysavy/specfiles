Name:		domoticz
Version:	3.4834
Release:	1%{?dist}
Summary:	Domoticz Home automation system

License:	GNU GPL 3
URL:		http://www.domoticz.com
Source0:	https://github.com/domoticz/domoticz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	make cmake gcc gcc-c++
BuildRequires:	git
BuildRequires:	boost-devel
BuildRequires:	openssl-devel
BuildRequires:	curl-devel
BuildRequires:	libstdc++-static
BuildRequires:  libusb-devel


%description


%prep
%setup -q


%build
cmake . -DCMAKE_BUILD_TYPE=Release
make


%install
%make_install


%define bindir /opt/domoticz


%files
%doc History.txt
%license License.txt
%{bindir}
#%{_bindir}/%{name}*
#%{_libdir}/%{name}.so.*


%changelog

