git checkout lab5

$dup = "Lab5_Project\Reem_Rashid_Alharbi_web-lab5\libraryproject"

if (Test-Path "$dup\apps\templates\bookmodule\lab5") {
    Move-Item -Force "$dup\apps\templates\bookmodule\lab5" "libraryproject\apps\templates\bookmodule\lab5"
}
if (Test-Path "$dup\apps\templates\layouts\base_html5.html") {
    Move-Item -Force "$dup\apps\templates\layouts\base_html5.html" "libraryproject\apps\templates\layouts\base_html5.html"
}
if (Test-Path "$dup\apps\static\main.css") {
    Move-Item -Force "$dup\apps\static\main.css" "libraryproject\apps\static\main.css"
}
if (Test-Path "$dup\apps\static\desert.jpg") {
    Move-Item -Force "$dup\apps\static\desert.jpg" "libraryproject\apps\static\desert.jpg"
}
if (Test-Path "$dup\apps\bookmodule\views.py") {
    Copy-Item -Force "$dup\apps\bookmodule\views.py" "libraryproject\apps\bookmodule\views.py"
}
if (Test-Path "$dup\apps\bookmodule\urls.py") {
    Copy-Item -Force "$dup\apps\bookmodule\urls.py" "libraryproject\apps\bookmodule\urls.py"
}
if (Test-Path "Lab5_Project") {
    Remove-Item -Recurse -Force "Lab5_Project"
}

git add -A
git commit -m "Fix lab5 branch: remove duplicate folder, place Lab5 pages correctly"
git push

git checkout main
git stash drop 2>$null
git merge lab5 --no-edit
git push

Write-Host "DONE. Repo is now clean on branch main with Lab1-5."