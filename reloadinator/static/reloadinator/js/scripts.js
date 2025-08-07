// Reloadinator JavaScript Functions
class Reloadinator {
    constructor() {
        this.clickCount = 0;
        this.init();
    }

    init() {
        this.addLoadingAnimation();
        this.setupKeyboardShortcuts();
        this.setupBadgeInteraction();
        this.setupReloadButton();
        this.setupEasterEggs();
    }

    // Add loading animation on page load
    addLoadingAnimation() {
        document.addEventListener('DOMContentLoaded', () => {
            const loadingElement = document.querySelector('.loading');
            if (loadingElement) {
                loadingElement.style.opacity = '1';
            }
        });
    }

    // Setup keyboard shortcuts
    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Ctrl/Cmd + R with animation
            if (e.key === 'r' && (e.ctrlKey || e.metaKey)) {
                this.animatedReload();
                e.preventDefault();
            }

            // Space bar for fun interaction
            if (e.key === ' ') {
                this.triggerConfetti();
                e.preventDefault();
            }
        });
    }

    // Animated reload function
    animatedReload() {
        const card = document.querySelector('.card');
        if (card) {
            card.classList.add('animate__animated', 'animate__rotateOut');
            setTimeout(() => {
                window.location.reload();
            }, 500);
        } else {
            window.location.reload();
        }
    }

    // Setup badge click interaction
    setupBadgeInteraction() {
        const badge = document.querySelector('.badge');
        if (badge) {
            badge.addEventListener('click', () => {
                this.clickCount++;
                this.animateBadgeClick(badge);

                // Special effects for multiple clicks
                if (this.clickCount > 5) {
                    this.showClickMessage();
                }
            });

            // Add hover effect
            badge.addEventListener('mouseenter', () => {
                badge.style.transform = 'scale(1.1) rotate(5deg)';
            });

            badge.addEventListener('mouseleave', () => {
                badge.style.transform = 'scale(1) rotate(0deg)';
            });
        }
    }

    // Animate badge click
    animateBadgeClick(badge) {
        const scale = 1 + (this.clickCount * 0.05);
        badge.style.transform = `scale(${Math.min(scale, 1.3)}) rotate(${this.clickCount * 10}deg)`;

        setTimeout(() => {
            badge.style.transform = 'scale(1) rotate(0deg)';
        }, 300);

        // Add particle effect
        this.createParticles(badge);
    }

    // Create particle effect
    createParticles(element) {
        const rect = element.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        for (let i = 0; i < 5; i++) {
            setTimeout(() => {
                this.createParticle(centerX, centerY);
            }, i * 50);
        }
    }

    createParticle(x, y) {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: fixed;
            left: ${x}px;
            top: ${y}px;
            width: 6px;
            height: 6px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            border-radius: 50%;
            pointer-events: none;
            z-index: 1000;
            animation: particle-float 1s ease-out forwards;
        `;

        document.body.appendChild(particle);

        // Remove particle after animation
        setTimeout(() => {
            if (particle.parentNode) {
                particle.parentNode.removeChild(particle);
            }
        }, 1000);
    }

    // Setup reload button
    setupReloadButton() {
        const reloadBtn = document.querySelector('.btn-reload');
        if (reloadBtn) {
            reloadBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.animatedReload();
            });
        }
    }

    // Show click message
    showClickMessage() {
        const existingMessage = document.querySelector('.click-message');
        if (existingMessage) return;

        const message = document.createElement('div');
        message.className = 'click-message alert alert-info animate__animated animate__bounceIn mt-2';
        message.innerHTML = `
            <small>
                <i class="bi bi-mouse"></i>
                You've clicked ${this.clickCount} times! Curious, aren't we? 😄
            </small>
        `;

        const cardBody = document.querySelector('.card-body');
        if (cardBody) {
            cardBody.appendChild(message);

            // Remove message after 3 seconds
            setTimeout(() => {
                message.classList.add('animate__fadeOut');
                setTimeout(() => {
                    if (message.parentNode) {
                        message.parentNode.removeChild(message);
                    }
                }, 500);
            }, 3000);
        }
    }

    // Easter eggs and fun interactions
    setupEasterEggs() {
        // Konami code easter egg
        let konamiCode = [];
        const konamiSequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65]; // ↑↑↓↓←→←→BA

        document.addEventListener('keydown', (e) => {
            konamiCode.push(e.keyCode);
            if (konamiCode.length > konamiSequence.length) {
                konamiCode.shift();
            }

            if (JSON.stringify(konamiCode) === JSON.stringify(konamiSequence)) {
                this.activateKonamiMode();
            }
        });

        // Random background color change on long idle
        let idleTimer;
        document.addEventListener('mousemove', () => {
            clearTimeout(idleTimer);
            idleTimer = setTimeout(() => {
                this.randomBackgroundShift();
            }, 30000); // 30 seconds of idle
        });
    }

    // Activate Konami code effects
    activateKonamiMode() {
        document.body.style.animation = 'rainbow 2s infinite';

        const message = document.createElement('div');
        message.className = 'alert alert-success animate__animated animate__tada position-fixed top-50 start-50 translate-middle';
        message.style.zIndex = '9999';
        message.innerHTML = `
            <h4><i class="bi bi-trophy"></i> KONAMI CODE ACTIVATED!</h4>
            <p>You've unlocked the secret developer mode! 🎮</p>
        `;

        document.body.appendChild(message);

        setTimeout(() => {
            document.body.style.animation = '';
            if (message.parentNode) {
                message.parentNode.removeChild(message);
            }
        }, 5000);
    }

    // Trigger confetti effect
    triggerConfetti() {
        // Simple confetti simulation
        for (let i = 0; i < 20; i++) {
            setTimeout(() => {
                this.createConfetti();
            }, i * 30);
        }
    }

    createConfetti() {
        const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7', '#dda0dd'];
        const confetti = document.createElement('div');

        confetti.style.cssText = `
            position: fixed;
            left: ${Math.random() * 100}vw;
            top: -10px;
            width: 10px;
            height: 10px;
            background: ${colors[Math.floor(Math.random() * colors.length)]};
            border-radius: ${Math.random() > 0.5 ? '50%' : '0'};
            pointer-events: none;
            z-index: 1000;
            animation: confetti-fall ${2 + Math.random() * 3}s linear forwards;
        `;

        document.body.appendChild(confetti);

        setTimeout(() => {
            if (confetti.parentNode) {
                confetti.parentNode.removeChild(confetti);
            }
        }, 5000);
    }

    // Random background shift for idle users
    randomBackgroundShift() {
        const gradients = [
            'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
            'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
            'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
            'linear-gradient(135deg, #fa709a 0%, #fee140 100%)'
        ];

        const randomGradient = gradients[Math.floor(Math.random() * gradients.length)];
        document.body.style.background = randomGradient;
        document.body.style.transition = 'background 2s ease';
    }
}

// Add CSS animations via JavaScript
const styles = `
    @keyframes particle-float {
        0% {
            transform: translate(0, 0) scale(1);
            opacity: 1;
        }
        100% {
            transform: translate(${Math.random() * 200 - 100}px, ${Math.random() * 200 - 100}px) scale(0);
            opacity: 0;
        }
    }

    @keyframes confetti-fall {
        0% {
            transform: translateY(-100vh) rotate(0deg);
        }
        100% {
            transform: translateY(100vh) rotate(720deg);
        }
    }

    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
`;

// Inject styles
const styleSheet = document.createElement('style');
styleSheet.textContent = styles;
document.head.appendChild(styleSheet);

// Initialize Reloadinator when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new Reloadinator();
});

// Export for potential module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = Reloadinator;
}