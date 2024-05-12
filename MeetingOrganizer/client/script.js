const mainContent = document.getElementById('mainContent');

// Sayfa yüklendiğinde varsayılan olarak toplantı kayıt formunu yükle
document.addEventListener('DOMContentLoaded', function() {
    loadPage('meeting_registration');
});

function navigateTo(page) { //Nav bardaki click olayına göre sayfalara yönlendirmek için 
    loadPage(page);
    if (page === 'meeting_list') {
        fetchMeetingList(); // Toplantı listesini almak için
    }
}

// Belirtilen HTML dosyasının içeriğini yükleyen fonksiyon
function loadPage(page) {
    fetch(page + '.html')
    .then(response => response.text())
    .then(html => {
        mainContent.innerHTML = html;
        addFormEventListeners(); 
    })
    .catch(error => console.log('Error loading page:', error));
}

function addFormEventListeners() {
    const meetingForm = document.getElementById('meetingForm');
    const updateForm = document.getElementById('updateForm');
    const deleteMeetingButton = document.getElementById('deleteMeetingButton');

    if (meetingForm) {
        // Meeting Kayıt Formu gönderildiğinde
        meetingForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Formun submit işlemini durdur
            // Formdaki verileri al
            const topic = document.getElementById('topic').value;
            const date = document.getElementById('date').value;
            const startTime = document.getElementById('startTime').value;
            const endTime = document.getElementById('endTime').value;
            const participants = document.getElementById('participants').value;
            // POST request için JSON obje verisi:
            const data = {
                topic: topic,
                date: date,
                startTime: startTime,
                endTime: endTime,
                participants: participants
            };
            // Burada HTTP POST isteği yapılacak ve veriler sunucuya gönderilecek
            console.log('Meeting form data:', data);
            fetch('http://127.0.0.1:5000/api/meetings', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                if (response.ok) {
                    // Başarılı ise kullanıcıya bilgi ver
                    alert('Meeting successfully registered!');
                    meetingForm.reset();// Formu sıfırla
                } else {
                    // Hata durumunda kullanıcıya bilgi ver
                    alert('Error registering meeting!');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error registering meeting! Please try again later.');
            });
        });
    }

    if (updateForm) {
        // Toplantı Güncelleme Formu gönderildiğinde
        updateForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Formun submit işlemini durdur

            // Formdaki verileri al
            const meeting_id = document.getElementById('meetingID').value;
            const updateTopic = document.getElementById('updateTopic').value;
            const updateDate = document.getElementById('updateDate').value;
            const updateStartTime = document.getElementById('updateStartTime').value;
            const updateEndTime = document.getElementById('updateEndTime').value;
            const updateParticipants = document.getElementById('updateParticipants').value;
            // PUT request için JSON verisi oluştur
            const updateData = {
                updateTopic: updateTopic,
                updateDate: updateDate,
                updateStartTime: updateStartTime,
                updateEndTime: updateEndTime,
                updateParticipants: updateParticipants
            };

            // Burada HTTP PUT isteği yapılacak ve veriler sunucuya gönderilecek
            console.log('Meeting update data:', updateData);
            console.log('Güncelleme isteği URL:', `http://127.0.0.1:5000/api/meetings/${meeting_id}`);
            //Sunucuya PUT request gönder
            fetch(`http://127.0.0.1:5000/api/meetings/${meeting_id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(updateData)
            })
            .then(response => {
                if (response.ok) {
                    // Başarılı ise kullanıcıya bilgi ver
                    alert('Meeting successfully updated!');
                    // Formu sıfırla
                    updateForm.reset();
                } else {
                    // Hata durumunda kullanıcıya bilgi ver
                    alert('Error updating meeting!');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error updating meeting! Please try again later.');
            });
        });
    }

    if (deleteMeetingButton) {
        // Meeting Delete işlevi
        deleteMeetingButton.addEventListener('click', function() {
            const meeting_id = document.getElementById('meetingID').value;

            // DELETE request gönder
            fetch(`http://127.0.0.1:5000/api/meetings/${meeting_id}`, {
                method: 'DELETE'
            })
            .then(response => {
                if (response.ok) {
                    alert('Meeting successfully deleted!');
                    if (updateForm) {
                        updateForm.reset();
                    }
                } else {
                    alert('Error deleting meeting!');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error deleting meeting! Please try again later.');
            });
        });
    }
}

// Function to fetch and display meeting list
function fetchMeetingList() {
    // Sunucudan toplantı listesini GET request ile alınması
    fetch('http://127.0.0.1:5000/api/meetings')
        .then(response => response.json())
        .then(meetings => {
            const meetingList = document.getElementById('meetingList');
            meetingList.innerHTML = ''; // Önceki listeyi temizle
            // Her toplantı için bir list elemanı oluştur ve listeye ekle
            meetings.forEach(meeting => {
                const li = document.createElement('li');
                li.textContent = ` ${meeting.id} - ${meeting.topic} - ${meeting.date} (${meeting.start_time} - ${meeting.end_time})`;
                meetingList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error fetching meeting list! Please try again later.');
        });
}

