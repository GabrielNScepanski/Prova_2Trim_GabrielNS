const mesAniver = 2;
const meses = ["janeiro", "fevereiro"];

for (let mes = 1; mes <= 2; mes++) {
  if (mes === mesAniver) {
    console.log(`Nasci no mês ${mes} (${meses[mes - 1]})`);
  } else {
    console.log(`Não nasci no mês ${mes} (${meses[mes - 1]})`);
  }
}

