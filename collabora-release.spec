Name: collabora-release
Version: 0.0.1
Release: 1%{?dist}
Summary: Collabora repo for NethServer
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: nethserver-devtools

%description
NethServer Collabora repository installer

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update


%changelog
* Tue Sep 11 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-1
- First release
