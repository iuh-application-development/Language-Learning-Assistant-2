const dictUrl = "https://api.dictionaryapi.dev/api/v2/entries/en/";
const translateUrl = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=vi&dt=t&q=";
const result = document.getElementById("result");
const sound = document.getElementById("sound");
const btn = document.getElementById("search-btn");
const inputWord = document.getElementById("inp-word");

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

// Hàm tìm kiếm từ
async function searchWord() {
    let inpWord = inputWord.value.trim();
    
    // Kiểm tra nếu không có từ nào được nhập
    if (!inpWord) {
        result.innerHTML = `
            <div class="alert alert-warning" role="alert">
                <i class="fas fa-exclamation-circle me-2"></i>
                Vui lòng nhập từ cần tra cứu
            </div>`;
        return;
    }
    
    // Hiển thị trạng thái đang tìm kiếm
    result.innerHTML = `
        <div class="text-center py-4">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2">Đang tìm kiếm...</p>
        </div>`;
    
    try {
        // Encode URI để đảm bảo các ký tự đặc biệt được xử lý đúng
        const response = await fetch(encodeURI(`${dictUrl}${inpWord}`));
        
        // Kiểm tra nếu response không OK (status code không phải 2xx)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Kiểm tra nếu không có dữ liệu hoặc dữ liệu không như mong đợi
        if (!data || !Array.isArray(data) || data.length === 0) {
            throw new Error('Không tìm thấy từ trong từ điển');
        }
        
        // Kiểm tra các thuộc tính cần thiết có tồn tại không
        if (!data[0].meanings || data[0].meanings.length === 0 || 
            !data[0].meanings[0].definitions || data[0].meanings[0].definitions.length === 0) {
            throw new Error('Dữ liệu không đầy đủ');
        }
        
        // Lấy nghĩa tiếng Việt cho từ
        const mainDefinition = data[0].meanings[0].definitions[0].definition;
        const vietnameseMeaning = await translateToVietnamese(mainDefinition);
        
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

        // Kiểm tra âm thanh phát âm nếu có
        let phoneticText = '';
        let audioUrl = '';
        
        if (data[0].phonetic) {
            phoneticText = data[0].phonetic;
        } else if (data[0].phonetics && data[0].phonetics.length > 0) {
            for (const phonetic of data[0].phonetics) {
                if (phonetic.text) {
                    phoneticText = phonetic.text;
                }
                if (phonetic.audio) {
                    audioUrl = phonetic.audio;
                    break;
                }
            }
        }
        
        // Hiển thị kết quả
        result.innerHTML = `
            <div class="word-title mb-4 d-flex align-items-center">
                <h3 class="mb-0">${inpWord}</h3>
                ${audioUrl ? `
                <button class="btn btn-sm btn-outline-primary ms-3" onclick="playSound('${audioUrl}')">
                    <i class="fas fa-volume-up"></i>
                </button>` : ''}
            </div>
            <div class="word-details mb-4">
                <span class="badge bg-primary me-2">${data[0].meanings[0].partOfSpeech || 'N/A'}</span>
                <span class="text-muted">/${phoneticText || ''}/</span>
            </div>
            <div class="word-meaning mb-4">
                <h5 class="text-primary mb-3">Nghĩa:</h5>
                <div class="card bg-light">
                    <div class="card-body">
                        <p class="mb-2"><strong>English:</strong> ${mainDefinition}</p>
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

         // Cập nhật giá trị cho các trường ẩn một cách an toàn
         const questionField = document.getElementById("flashcard-question");
         const answerField = document.getElementById("flashcard-answer");
         const flashcardForm = document.getElementById("add-flashcard-form");
 
         if (questionField) questionField.value = inpWord;
         if (answerField) answerField.value = vietnameseMeaning;
 
         // Hiển thị form thêm flashcard nếu nó tồn tại
         if (flashcardForm) flashcardForm.style.display = "block";
         
    } catch (error) {
        console.error('Error:', error);
        result.innerHTML = `
            <div class="alert alert-danger" role="alert">
                <i class="fas fa-exclamation-circle me-2"></i>
                ${error.message || 'Không tìm thấy từ này trong từ điển'}
            </div>`;
    }
}

// Thêm sự kiện click cho nút tìm kiếm
btn.addEventListener("click", searchWord);

// Thêm sự kiện keypress cho ô input để bắt sự kiện Enter
inputWord.addEventListener("keypress", function(event) {
    // Kiểm tra nếu phím được nhấn là Enter (mã phím 13)
    if (event.key === "Enter") {
        // Hủy hành động mặc định của form (nếu có)
        event.preventDefault();
        // Gọi hàm tìm kiếm từ
        searchWord();
    }
});

// Xử lý sự kiện submit form thêm flashcard
document.getElementById("add-flashcard-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    
    try {
        const response = await fetch('/dictionary/', {  // Đường dẫn đến view dictionary
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Lấy CSRF token
            },
        });
        const result = await response.json();
        if (result.success) {
            alert('Flashcard đã được tạo thành công!');
        } else {
            alert('Có lỗi xảy ra: ' + result.error);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

// Hàm phát âm thanh từ URL
function playSound(audioUrl) {
    if (audioUrl) {
        const audio = new Audio(audioUrl);
        audio.play().catch(err => {
            console.error('Failed to play audio:', err);
        });
    }
}

// Hàm lấy CSRF token từ cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}