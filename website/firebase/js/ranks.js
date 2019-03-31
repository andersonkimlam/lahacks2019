
function loadRank() {
  var result = ['GLPG', 'PRGS', 'EXP', 'ATHM', 'BB', 'AMRN', 'CHWRF', 'KMX', 'HNNMY', 'LYFT', 'CELG', 'ALLO', 'IRWD', 'S', 'PDD', 'WB', 'BZUN', 'TTD', 'IMPUY', 'BPMC', 'JBSAY', 'TKGBY', 'GBOOF', 'TI-A', 'GRFS', 'AKBTY', 'IQ', 'NOAH', 'TME', 'MU', 'HKXCF', 'WDC', 'GFSZF', 'WLWHY', 'GDS', 'ICPT', 'AERI', 'HTHT', 'ALBKF', 'ETRN', 'KOS', 'BILI', 'SAIC', 'WUBA', 'BGNE', 'EDU', 'SEAS', 'BEST', 'HUYA', 'SINA', 'STX', 'JOBS', 'GH', 'YY', 'FSUGY', 'ALGN', 'ENIC', 'DNLI', 'GRUB', 'COHR', 'BKRKF', 'ZNH', 'BAYZF', 'STM', 'WK', 'RKLIF', 'ALNPY', 'SMFKY', 'LEVI', 'TDOC', 'BMA', 'TEAM', 'MKSI', 'MRNA', 'HNHPF', 'BACHF', 'VALE', 'CIG', 'OMAB', 'IMMU', 'SHAK', 'XLRN', 'LFC', 'FHL', 'ROG', 'CFX', 'INSM', 'TV', 'ASR', 'QFIN', 'PTLA', 'CCU', 'SID', 'CARG', 'AZUL', 'KSRYY', 'PCG', 'MMYT', 'NS-PB', 'LNG'];
  // document.createElement;
  var list = document.getElementsByClassName("rank");

  for(var i = 0; i < 15; i++) {
    list[i].innerHTML = result[i];
  }
}
  // var firebaseData = ["blah blah", "blah blah blah", "jadflkadsjf", "lsakdfj", "fdjf"];
  // document.createElement



  window.onload = loadRank;

// window.onload = loadRank;
