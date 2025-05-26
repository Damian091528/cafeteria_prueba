// Simulación de cómo se obtiene el rol desde el login (puedes reemplazar con datos reales)
const userID = localStorage.getItem("userID"); // ID guardado al iniciar sesión

function obtenerRolDesdeID(id) {
  if (!id) return "invitado";
  if (id.startsWith("S")) return "estudiante";
  if (id.startsWith("T")) return "trabajador";
  if (id.startsWith("A")) return "administración";
  if (id.startsWith("P")) return "profesor";
  return "desconocido";
}

const rol = obtenerRolDesdeID(userID);
document.getElementById("userRole").textContent = rol;
