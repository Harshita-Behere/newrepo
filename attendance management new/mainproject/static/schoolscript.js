function navigateTo(schoolName) {
  alert(`You selected: ${schoolName}`);
  // Example: Redirect based on school selection
  if (schoolName === 'School of Technology') {
      window.location.href = '/school-of-technology';
  } else if (schoolName === 'School of Forensic Science') {
      window.location.href = '/school-of-forensic-science';
  } else if (schoolName === 'School of Law') {
      window.location.href = '/school-of-law';
  }
}