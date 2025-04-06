const dictUrl = "https://api.dictionaryapi.dev/api/v2/entries/en/";
const translateUrl = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=vi&dt=t&q=";
const result = document.getElementById("result");
const sound = document.getElementById("sound");
const btn = document.getElementById("search-btn");

async function translateToVietnamese(text) {
    try {
        const response = await fetch(encodeURI(`${translateUrl}${text}`));
        const data = await response.json();
        return data[0][0][0];
    } catch (error) {
        console.error('Translation error:', error);
        return "Không thể dịch";
    }
}

btn.addEventListener("click", async () => {
    let inpWord = document.getElementById("inp-word").value;
    try {
        const response = await fetch(`${dictUrl}${inpWord}`);
        const data = await response.json();
        
        // Lấy nghĩa tiếng Việt cho từ
        const vietnameseMeaning = await translateToVietnamese(data[0].meanings[0].definitions[0].definition);
        
        // Tạo HTML cho các ví dụ
        let examplesHTML = '';
        const examples = data[0].meanings[0].definitions;
        for(let i = 0; i < Math.min(3, examples.length); i++) {
            if(examples[i].example) {
                const vietnameseExample = await translateToVietnamese(examples[i].example);
                examplesHTML += `
                    <div class="example-item mb-3">
                        <p class="mb-1"><i class="fas fa-angle-right text-primary me-2"></i>${examples[i].example}</p>
                        <p class="text-muted ms-4">${vietnameseExample}</p>
                    </div>`;
            }
        }

        result.innerHTML = `
            <div class="word-title mb-4">
                <h3 class="mb-0">${inpWord}</h3>
               
            </div>

            <div class="word-details mb-4">
                <span class="badge bg-primary me-2">${data[0].meanings[0].partOfSpeech}</span>
                <span class="text-muted">/${data[0].phonetic || ''}/</span>
            </div>

            <div class="word-meaning mb-4">
                <h5 class="text-primary mb-3">Nghĩa:</h5>
                <div class="card bg-light">
                    <div class="card-body">
                        <p class="mb-2"><strong>English:</strong> ${data[0].meanings[0].definitions[0].definition}</p>
                        <p class="mb-0"><strong>Tiếng Việt:</strong> ${vietnameseMeaning}</p>
                    </div>
                </div>
            </div>

            ${examplesHTML ? `
                <div class="word-examples">
                    <h5 class="text-primary mb-3">Ví dụ:</h5>
                    ${examplesHTML}
                </div>
            ` : ''}`;

        if(data[0].phonetics[0]?.audio) {
            sound.setAttribute("src", `https:${data[0].phonetics[0].audio}`);
        }
    } catch (error) {
        result.innerHTML = `
            <div class="alert alert-danger" role="alert">
                <i class="fas fa-exclamation-circle me-2"></i>
                Không tìm thấy từ này trong từ điển
            </div>`;
    }
});

function playSound() {
    sound.play();
}