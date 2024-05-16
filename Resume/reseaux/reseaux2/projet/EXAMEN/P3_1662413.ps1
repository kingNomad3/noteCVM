# Import user data from CSV
$utilisateurs = Import-Csv "E:\_S1_INFO\INFORMATIQUE_ETU_A2023.csv" -Delimiter ";"

foreach ($users in $utilisateurs) {
    $matricule = $users.MATRICULE
    $nomGroupe = ""

    # Determine the group and OU based on the matricule number
    if ($matricule -ge 70001 -and $matricule -le 70350) {
        $nomGroupe = "OU=Employes,OU=Programmeurs Python,OU=Utilisateurs"
    } elseif ($matricule -eq 70000) {
        $nomGroupe = "OU=Gestionnaires,OU=Programmeurs Python,OU=Utilisateurs"
    }

    if (![string]::IsNullOrWhiteSpace($nomGroupe)) {
        # Split the group name to extract the OU path parts
        $groupParts = $nomGroupe -split "/"
        $ouPath = "$nomGroupe,OU=DEPT1662413,DC=ETU1662413,DC=local"
	Write-Output $ouPath
        $password = ConvertTo-SecureString "ABC-123" -AsPlainText -Force
            New-ADUser -Name $users.MATRICULE `
             -SamAccountName $users.NOM `
             -UserPrincipalName "$($users.NOM)@ETU1662413.local" `
             -Path $ouPath `
             -GivenName $users.NOM `
             -Surname $users.PRENOM `
             -DisplayName "$($users.PRENOM) $($users.NOM)" `
             -AccountPassword $password `
             -PasswordNeverExpires $true `
             -Enabled $true
        
    }
}