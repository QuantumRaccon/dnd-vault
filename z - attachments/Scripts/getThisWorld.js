function getThisWorld (tp) {
    const thisFolder = tp.file.folder(false)
    if (thisFolder == "Los Esferones de Azhül"){
        return "Azhül";
    }
    else if (thisFolder == "Cronicas de Ghalmor") {
        return "Ghalmor"
    }

    return thisFolder;
}
module.exports = getThisWorld;