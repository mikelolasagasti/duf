# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/muesli/duf
%global goipath         github.com/muesli/duf
Version:                0.8.1

%gometa

%global goname          duf

%global common_description %{expand:
Disk Usage/Free Utility - a better 'df' alternative.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Disk Usage/Free Utility - a better 'df' alternative

License:        MIT and BSD

URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
# Current golang-github-jedib0t-pretty package is not versioned
sed -e 's:go-pretty/v6:go-pretty:' -i go.sum go.mod main.go table.go

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/duf %{goipath}

%install
%gopkginstall
install -m 0755 -vd                       %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/duf %{buildroot}%{_bindir}/
install -m 0755 -vd                       %{buildroot}%{_mandir}/man1
cp -a duf.1 %{buildroot}%{_mandir}/man1/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/duf
%{_mandir}/man1/duf.1*

%gopkgfiles

%changelog
%autochangelog
