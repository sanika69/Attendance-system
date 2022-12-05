const addButton = document.querySelector('#add');

const addNewNote = (text = '') => {
    const note = document.createElement('div');
    note.classList.add('note')

    const htmlData = `
    
    <div class="operation">
        <button class="edit"><i class="fas fa-edit"></i></button>
        <button class="delete"><i class="fas fa-trash-alt"></i></button>
    </div>
    <div class="main ${text ? "" : "hidden"}"></div>
    <textarea class=" ${text ? "hidden" : ""}" ></textarea>
`
    note.insertAdjacentHTML('afterbegin', htmlData);
    // console.log(note)

    //getting references
    const editButton = note.querySelector('.edit')
    const delGutton = note.querySelector('.delete')
    const MainDiv = note.querySelector('.main')
    const textarea = note.querySelector('textarea')

    //remove the note
    delGutton.addEventListener('click', () => {
        note.remove();
        updateLSDATA();
    });


    textarea.value = text;
    MainDiv.innerHTML = text;


    //toggle using edit button
    editButton.addEventListener('click', () => {
        MainDiv.classList.toggle('hidden');
        textarea.classList.toggle('hidden');
    })

    //storage function 
    const updateLSDATA = () => {
        const TextAre = document.querySelectorAll('textarea');

        const notes = [];

        TextAre.forEach((note) => {
            return notes.push(note.value);
        })
        localStorage.setItem('notes', JSON.stringify(notes));

    }


    textarea.addEventListener('change', (event) => {
        const value = event.target.value;
        console.log(value);

        MainDiv.innerHTML = value;
        updateLSDATA();

    })
    

    let div=document.querySelector(".add");

    div.appendChild(note);

}




//getting data back from localStroge

const notes = JSON.parse(localStorage.getItem('notes'))

if (notes) {
    notes.forEach((note) => addNewNote(note))
}



addButton.addEventListener('click', () => addNewNote());
