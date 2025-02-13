// let sortOrder = {}; // Menyimpan state sorting untuk setiap kolom

// function sortTable(columnIndex) {
//     let table = document.querySelector("table tbody");
//     let rows = Array.from(table.querySelectorAll("tr"));

//     // Cek urutan sorting (default: ascending)
//     let order = sortOrder[columnIndex] === "asc" ? "desc" : "asc";
//     sortOrder[columnIndex] = order;

//     // Sorting data berdasarkan tipe data (angka, teks, atau tanggal)
//     rows.sort((a, b) => {
//         let valA = a.cells[columnIndex].innerText.trim();
//         let valB = b.cells[columnIndex].innerText.trim();

//         if (columnIndex === 0) {
//             return order === "asc" ? valA - valB : valB - valA; // Sort angka
//         } else if (columnIndex === 4) {
//             return order === "asc" ? new Date(valA) - new Date(valB) : new Date(valB) - new Date(valA); // Sort tanggal
//         } else {
//             return order === "asc" ? valA.localeCompare(valB) : valB.localeCompare(valA); // Sort teks
//         }
//     });

//     // Tambahkan kembali baris yang telah diurutkan
//     table.innerHTML = "";
//     rows.forEach(row => table.appendChild(row));
// }

function confirmDelete(id, type) {
    Swal.fire({
        title: "Apakah Anda yakin?",
        text: "Data ini akan dihapus secara permanen!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#d33",
        cancelButtonColor: "#3085d6",
        confirmButtonText: "Ya, Hapus!",
        cancelButtonText: "Batal"
    }).then((result) => {
        if (result.isConfirmed) {
            let deleteUrl = "";

            if (type === 'kategori') {
                deleteUrl = `/kategori/hapus/${encodeURIComponent(id)}/`;
            } else if (type === 'buku') {
                deleteUrl = `/buku/hapus/${encodeURIComponent(id)}/`;
            }

            if (deleteUrl) {
                window.location.href = deleteUrl;
            }
        }
    });
}